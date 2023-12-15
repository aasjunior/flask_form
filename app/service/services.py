from model.schemas import PacienteForm
import requests, json

def create_paciente(data):
    form = PacienteForm(data)
    if form.validate():
        try:
            response = requests.post('http://localhost:8000/pacientes/cadastro', data=json.dumps(form.data), headers={'Content-Type': 'application/json'})
            
            # irá lançar uma exceção se a resposta contiver um código de status de erro HTTP
            response.raise_for_status()
            return True, response.json()
        
        except requests.exceptions.RequestException as e:
            # lidar com erros de rede, como problemas de conexão
            return False, str(e)
        
        except ValueError:
            # lidar com erros de decodificação JSON
            return False, 'Erro ao decodificar a resposta da API'
    else:
        return False, form.errors