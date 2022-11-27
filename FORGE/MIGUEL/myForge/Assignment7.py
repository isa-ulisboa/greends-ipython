import pandas as pd
import myFunctions
import matplotlib.pyplot as plt

Current = pd.read_csv('Climate_hisafe_knmievaluation_daily_from_01-01-1981_to_31-12-2010.csv', skiprows=[0])
Future = pd.read_csv('Climate_hisafe_knmircp85_daily_from_01-01-2006_to_31-12-2100.csv', skiprows=[0])

# Calculate VPD with pandas (your vpd function should work with numpy instead math library)
# The following creates an additional column called "VPD" where your function is used
Current["VPD"] = myFunctions.calculate_vpd_7(Current["tasmax"],Current["tasmin"],Current["hurs"] )
Future["VPD"] = myFunctions.calculate_vpd_7(Future["tasmax"],Future["tasmin"],Future["hurs"] )

# Conjunto de dados para o Futuro

Future_2031_2060 = Future[(Future["Year"] >= 2031) & (Future["Year"] <= 2060)]

# Médias para Atual e Futuro

avg_Current = Current.groupby(["Month"]).mean()
avg_monthly_Future = Future_2031_2060.groupby(["Month"]).mean()


# Criar Gráfico com matplot

avg_Current["VPD"].plot(label = "Current vpd", color = "green")
avg_monthly_Future["VPD"].plot(label = "Future vpd", color = "blue")

# Titlo
plt.title("Average vapor deficit pressure 1981-2010 and 2031-2060 ")

# Nomes para os eixos
plt.xlabel("Month")
plt.ylabel("vpd (kPa)")

#Legenda do Gráfico
plt.legend()

#Ver Gráfico

plt.show()

