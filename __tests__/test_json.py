import sys
import os

# Obtendo o caminho absoluto do diretório atual (__tests__) e adicionando o diretório pai (SecretCure) ao PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.json_util import JSONUtil

def test_read_user_infos_json():
    dados_json = JSONUtil.loadJson('user_infos.json')
    assert len(dados_json['levels_allowed']) > 0
    assert len(dados_json['user_info']['name']) != ''
    assert len(dados_json['user_info']['email']) != ''

def test_create_json():
    fake_data = {
        'title': 'Fake json',
        'created': True
    }

    JSONUtil.createJson(fake_data, 'fake.json')

