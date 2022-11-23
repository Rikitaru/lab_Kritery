import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

correlation1 = pd.read_csv('correl\GAZP_211121_221122.csv', sep=';')
correlation2 = pd.read_csv('correl\IRKT_211121_221122.csv', sep=';')
correlation3 = pd.read_csv('correl\MGNT_211121_221122.csv', sep=';')
correlation4 = pd.read_csv('correl\MOEX.CBOM_SMAL_211121_221122.csv', sep=';')
correlation5 = pd.read_csv('correl\MOEX.DIOD_SMAL_211121_221122.csv', sep=';')
correlation6 = pd.read_csv('correl\MOEX.DSKY_SMAL_211121_221122.csv', sep=';')
correlation7 = pd.read_csv('correl\MOEX_211121_221122.csv', sep=';')
correlation8 = pd.read_csv('correl\MTSS_211121_221122.csv', sep=';')
correlation9 = pd.read_csv('correl\SIBN_211121_221122.csv', sep=';')
correlation10 = pd.read_csv('correl\TGKD_211121_221122.csv', sep=';')

print("####################1####################\n", correlation1.corr())
print("####################2####################\n", correlation2.corr())
print("####################3####################\n", correlation3.corr())
print("####################4####################\n", correlation4.corr())
print("####################5####################\n", correlation5.corr())
print("####################6####################\n", correlation6.corr())
print("####################7####################\n", correlation7.corr())
print("####################8####################\n", correlation8.corr())
print("####################9####################\n", correlation9.corr())
print("####################10####################\n", correlation10.corr())

def image1():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation1.corr(), xticklabels=correlation1.corr().columns, yticklabels=correlation1.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation1.select_dtypes(['number']).shape[1]), correlation1.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation1.select_dtypes(['number']).shape[1]), correlation1.select_dtypes(['number']).columns, fontsize=14)
    plt.title('GAZP', fontsize=17)
    plt.show()
def image2():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation2.corr(), xticklabels=correlation2.corr().columns, yticklabels=correlation2.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation2.select_dtypes(['number']).shape[1]), correlation2.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation2.select_dtypes(['number']).shape[1]), correlation2.select_dtypes(['number']).columns, fontsize=14)
    plt.title('IRKT', fontsize=16)
    plt.show()
def image3():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation3.corr(), xticklabels=correlation3.corr().columns, yticklabels=correlation3.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation3.select_dtypes(['number']).shape[1]), correlation3.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation3.select_dtypes(['number']).shape[1]), correlation3.select_dtypes(['number']).columns, fontsize=14)
    plt.title('MGNT', fontsize=16)
    plt.show()
def image4():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation4.corr(), xticklabels=correlation4.corr().columns, yticklabels=correlation4.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation4.select_dtypes(['number']).shape[1]), correlation4.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation4.select_dtypes(['number']).shape[1]), correlation4.select_dtypes(['number']).columns, fontsize=14)
    plt.title('MOEX.CBOM_SMAL', fontsize=16)
    plt.show()
def image5():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation5.corr(), xticklabels=correlation1.corr().columns, yticklabels=correlation5.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation5.select_dtypes(['number']).shape[1]), correlation5.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation5.select_dtypes(['number']).shape[1]), correlation5.select_dtypes(['number']).columns, fontsize=14)
    plt.title('MOEX.DIOD_SMAL', fontsize=16)
    plt.show()
def image6():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation6.corr(), xticklabels=correlation6.corr().columns, yticklabels=correlation6.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation6.select_dtypes(['number']).shape[1]), correlation6.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation6.select_dtypes(['number']).shape[1]), correlation6.select_dtypes(['number']).columns, fontsize=14)
    plt.title('MOEX.DSKY_SMAL', fontsize=16)
    plt.show()
def image7():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation7.corr(), xticklabels=correlation7.corr().columns, yticklabels=correlation7.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation7.select_dtypes(['number']).shape[1]), correlation7.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation7.select_dtypes(['number']).shape[1]), correlation7.select_dtypes(['number']).columns, fontsize=14)
    plt.title('MOEX', fontsize=16)
    plt.show()
def image8():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation8.corr(), xticklabels=correlation8.corr().columns, yticklabels=correlation8.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation8.select_dtypes(['number']).shape[1]), correlation8.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation8.select_dtypes(['number']).shape[1]), correlation8.select_dtypes(['number']).columns, fontsize=14)
    plt.title('MTSS', fontsize=16)
    plt.show()
def image9():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation9.corr(), xticklabels=correlation9.corr().columns, yticklabels=correlation9.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation9.select_dtypes(['number']).shape[1]), correlation9.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation9.select_dtypes(['number']).shape[1]), correlation9.select_dtypes(['number']).columns, fontsize=14)
    plt.title('SIBN', fontsize=16)
    plt.show()
def image10():
    plt.figure(figsize=(7, 7))
    sns.heatmap(correlation10.corr(), xticklabels=correlation10.corr().columns, yticklabels=correlation10.corr().columns, cmap='RdYlGn', center=0, annot=True)
    plt.xticks(range(correlation10.select_dtypes(['number']).shape[1]), correlation10.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(correlation10.select_dtypes(['number']).shape[1]), correlation10.select_dtypes(['number']).columns, fontsize=14)
    plt.title('TGKD', fontsize=16)
    plt.show()

image1()
image2()
image3()
image4()
image5()
image6()
image7()
image8()
image9()
image10()