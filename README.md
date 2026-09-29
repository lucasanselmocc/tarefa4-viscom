# Tarefa 4 - Atenuação de ruído

## Pré-requisitos

opencv-python
numpy
matplotlib

```bash
pip install -r requirements.txt
```

O programa também utiliza `sys.argv` para receber os argumentos pela linha de comand.

## Como executar

Primeiro, gere as seis imagens com ruído:

```bash
gerarImagens.sh
```

Depois, execute o programa informando a imagem original e o valor de `k`. Ex.:

```bash
python3 atenuarRuido.py cristo.jpg 0
```

O programa mostra a imagem com ruído e a imagem filtrada lado a lado, juntamente com o PSNR.