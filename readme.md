# Scanning mutagenesis 

## Functionality
Generating batch of mutated sequences for given protein coding sequences. All codons except start and stop codon will be changed into alanine(GCG). If a codon is already alanine, it will be changed into lysine(AAA). Then add adapter sequences to the both ends of the sequence for PCR or other molecular modification.

## Prerequisite
Python 3.X  

#### The following libraries are needed
pandas  
pathlib  
os
## Usage
1.Fill in the protein name, sequence, upstream adapter and downstream adapter information in the table “sequences.xlsx". Format can be found in the example file. You can fill multiple proteins at the same time. Place this file in the same directory as main.py.  
2.Run the script. You can just open the script in your IDE(VS code, spyder, pycharm...) and click 'run'. Also you can run from the console using this command 'python main.py'  
3.The mutant sequences will be generated in the same directory. Each protein in the input “sequences.xlsx" will generate a file, storing all mutated sequences. (e.g, MinE protein will generate a new file called 'MinE_mutants.xlsx')


# 扫描诱变

## 功能描述
为给定蛋白质编码序列批量生成突变序列。除起始密码子和终止密码子外，所有密码子都将被替换为丙氨酸密码子(GCG)。若密码子原本即为丙氨酸，则将其替换为赖氨酸密码子(AAA)。随后在序列两端添加接头序列，用于PCR或其他分子修饰。

## 环境要求
Python 3.X  

#### 需要安装以下库
pandas  
pathlib  
os

## 使用方法
1. 在"sequences.xlsx"表格中填写蛋白质名称、序列、上游接头和下游接头信息。格式请参照示例文件，可同时填写多个蛋白质信息。请将该文件与main.py置于同一目录下。  
2. 运行脚本。可在IDE（VS code、spyder、pycharm等）中直接打开脚本点击"运行"，也可在控制台中使用命令'python main.py'运行。  
3. 突变序列将在同一目录下生成。输入文件"sequences.xlsx"中的每个蛋白质都会生成一个独立文件，存储所有突变序列（例如：MinE蛋白将生成名为'MinE_mutants.xlsx'的新文件）。