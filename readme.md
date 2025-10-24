# Scanning mutagenesis 

## Functionality
Generating batch of mutated sequences for given protein coding sequences. All codons except start and stop codon will be changed into alanine(GCG). If a codon is already alanine, it will be changed into lysine(AAA). 

## Prerequisite
Python 3.X  

#### The following libraries are needed
pandas  
pathlib  
os
## Usage
1.Fill in the protein name and sequence information in the table “sequences.xlsx". You can fill multiple proteins at the same time. Place this file in the same directory as main.py.  
2.Run the script. You can just open the script in your IDE(VS code, spyder, pycharm...) and click 'run'. Also you can run from the console using this command 'python main.py'  
3.The mutant sequences will be generated in the same directory. Each protein in the input “sequences.xlsx" will generate a file, storing all mutated sequences. (e.g, MinE protein will generate a new file called 'MinE_mutants.xlsx')


# 扫描诱变

## 功能
为给定的蛋白质编码序列生成批量突变序列。除起始密码子和终止密码子外，所有密码子都将变为丙氨酸(GCG)。如果某个密码子已经是丙氨酸，则将其变为赖氨酸(AAA)。

## 环境要求
Python 3.X

#### 需要安装以下库
pandas  
pathlib  
os

## 使用方法
1. 在"sequences.xlsx"表格中填写蛋白质名称和序列信息。你可以一次填写多个蛋白的信息。将此文件与main.py放在同一目录下。  
2. 运行脚本。您可以在IDE中打开脚本并点击"运行"，也可以使用控制台命令'python main.py'来运行。  
3. 突变序列将在同一目录中生成。输入文件"sequences.xlsx"中的每个蛋白质都会生成一个文件，存储所有突变序列。（例如，MinE蛋白将生成一个名为'MinE_mutants.xlsx'的新文件）