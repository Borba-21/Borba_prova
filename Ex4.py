#=========================================================================

#Exercício 4

import pandas as pd
import numpy as np

linhas = [f"hora_{i}" for i in range(1, 11)]
colunas = ["us-east-1", "us-west-2", "eu-central-1", "sa-east-1", "ap-southeast-1"]
dados = np.random.randint(0, 101, size=(10, 5))
df = pd.DataFrame(dados, index=linhas, columns=colunas)

print(df)

#=========================================================================