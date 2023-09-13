import boto3
import os
import datetime

aws_access_key_id = 'ASIAZTYZGHJ6GSEZURA4'
aws_secret_access_key = 'GmL54w9lrcclskhsG2+mTuhMUDCPIsHFepMeS+ll'
s3_bucket_name = 'data-lake-do-fulano'

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

local_csv_directory = 'D:/DEV/Data & Analytics - PB - AWS Compass UOL/Compass-UOL-PB/Sprint 7/Desafio/Filmes+e+Series'


def upload_to_s3(local_file_path, s3_key):
    try:
        today = datetime.date.today()
        year, month, day = today.year, today.month, today.day

        s3_path = f'Raw/Local/CSV/{s3_key}/{year}/{month:02d}/{day:02d}/{s3_key}.csv'

        s3.upload_file(local_file_path, s3_bucket_name, s3_path)
        print(
            f"Arquivo {local_file_path} carregado com sucesso para o S3 como {s3_path}")
    except Exception as e:
        print(f"Erro ao carregar arquivo {local_file_path} para S3: {str(e)}")


def main():
    for root, _, files in os.walk(local_csv_directory):
        for file in files:
            if file.endswith(".csv"):
                local_file_path = os.path.join(root, file)
                s3_key = os.path.splitext(file)[0]
                upload_to_s3(local_file_path, s3_key)


if __name__ == "__main__":
    main()
