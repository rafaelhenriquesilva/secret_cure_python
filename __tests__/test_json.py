import sys
import os

# Obtendo o caminho absoluto do diretório atual (__tests__) e adicionando o diretório pai (SecretCure) ao PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.json_util import JSONUtil
from src.useCases.user_use_case import UserUseCase
from src.models.user_model import UserInfo

def test_read_user_infos_json():
    data_json = JSONUtil.loadJson('user_infos.json')
    assert len(data_json['levels_allowed']) > 0
    assert len(data_json['user_info']['name']) != ''
    assert len(data_json['user_info']['email']) != ''

def test_create_json():
    data_json = JSONUtil.loadJson('user_infos.json')
    JSONUtil.createJson(data_json, 'fake.json')
    fake_data_json = JSONUtil.loadJson('user_infos.json')
    assert len(fake_data_json['levels_allowed']) > 0
    assert len(fake_data_json['user_info']['name']) != ''
    assert len(fake_data_json['user_info']['email']) != ''    

def test_change_user_info_and_json():
    fake_data_json = JSONUtil.loadJson('user_infos.json')
    user_info = UserInfo('Test', 'test@mail.com', 1)
    fake_data_json = UserUseCase.updateUserInfo(user_info, fake_data_json)
    JSONUtil.createJson(fake_data_json, 'fake.json')

    update_data_json = JSONUtil.loadJson('fake.json')
    assert update_data_json['user_info']['name'] == user_info.name
    assert update_data_json['user_info']['email'] == user_info.email
    assert update_data_json['user_info']['level'] == user_info.level

    
