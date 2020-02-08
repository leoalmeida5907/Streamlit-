import os
import streamlit as st 


import pandas as pd 


import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 

def main():
	
	st.title("Projeto Integrador")

	html_temp = """
	<div style="background-color:#00bfff;"><p style="color:white;font-size:50px;padding:10px">Grupo 100Vies</p></div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)

	def file_selector(folder_path='./datasets'):
		filenames = os.listdir(folder_path)
		selected_filename = st.selectbox("Selecione um arquivo",filenames)
		return os.path.join(folder_path,selected_filename)

	filename = file_selector()
	st.info("Você selecionou {}".format(filename))

	
	# Ler dados
	df = pd.read_csv(filename)

	# Mostrar conjunto de dados
	if st.checkbox("Mostrar conjunto de dados"):
		number = st.number_input("Número de linhas para exibir",1,200)
		st.dataframe(df.head(number))

	
	# Mostrar colunas
	if st.button("Nomes das colunas"):
		st.write(df.columns)

	# Mostrar Forma
	if st.checkbox("Forma do conjunto de dados"):
		data_dim = st.radio("Mostrar dimensão por",("Linhas","Colunas"))
		if data_dim == 'Linhas':
			st.text("Numero de linhas")
			st.write(df.shape[0])
		elif data_dim == 'Colunas':
			st.text("Numero de colunas")
			st.write(df.shape[1])
		else:
			st.write(df.shape)

	# Select Columns
	if st.checkbox("Selecionar colunas para mostrar"):
		all_columns = df.columns.tolist()
		selected_columns = st.multiselect("Selecione",all_columns)
		new_df = df[selected_columns]
		st.dataframe(new_df)

	# Mostrar valores
	if st.button("Contagens de valor"):
		st.text("Contagens de valor por destino / classe")
		st.write(df.iloc[:,-1].value_counts())
	
	# Mostrar tipos de dados
	if st.button("Tipos de dados"):
		st.write(df.dtypes)
	
	# Mostrar Resumo
	if st.checkbox("Resumo"):
		st.write(df.describe().T)

	# Gráfico e visualização
	st.subheader("Visualização de dados")
	# Correlação
	# Seaborn Plot
	if st.checkbox("Gráfico de Correlação [Seaborn]"):
		st.write(sns.heatmap(df.corr(),annot=True))
		st.pyplot()

	# Contagem
	if st.checkbox("Gráfico de contagens de valor"):
		st.text("Contagens de valor por destino")
		all_columns_names = df.columns.tolist()
		primary_col = st.selectbox("Coluna Primária a Agrupar",all_columns_names)
		selected_columns_names = st.multiselect("Selecionar colunas",all_columns_names)
		if st.button("Gráfico"):
			st.text("Gerar Gráfico")
			if selected_columns_names:
				vc_plot = df.groupby(primary_col)[selected_columns_names].count()
			else:
				vc_plot = df.iloc[:,-1].value_counts()
			st.write(vc_plot.plot(kind="bar"))
			st.pyplot()

	# Gráfico personalizável

	st.subheader("Gráfico personalizável")
	all_columns_names = df.columns.tolist()
	type_of_plot = st.selectbox("Selecione o tipo de plotagem",["area","bar","line","hist","box","kde"])
	selected_columns_names = st.multiselect("Selecionar colunas a serem plotadas",all_columns_names)

	if st.button("Gerar Gráfico"):
		st.success("Gerando plotagem personalizável de {} para {}".format(type_of_plot,selected_columns_names))

		# Plot por Streamlit
		if type_of_plot == 'area':
			cust_data = df[selected_columns_names]
			st.area_chart(cust_data)

		elif type_of_plot == 'bar':
			cust_data = df[selected_columns_names]
			st.bar_chart(cust_data)

		elif type_of_plot == 'line':
			cust_data = df[selected_columns_names]
			st.line_chart(cust_data)

		# Gráfico personalizado
		elif type_of_plot:
			cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
			st.write(cust_plot)
			st.pyplot()

	if st.button("Obrigado"):
		st.balloons()



if __name__ == '__main__':
	main()
