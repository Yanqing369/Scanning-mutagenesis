import pandas as pd
import os
from pathlib import Path
script_dir = Path(__file__).parent
os.chdir(script_dir)


# 定义密码子表
CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

# 定义起始密码子和终止密码子
START_CODONS = ['ATG']
STOP_CODONS = ['TAA', 'TAG', 'TGA']

def translate_codon(codon):
    """翻译密码子为氨基酸"""
    return CODON_TABLE.get(codon.upper(), 'X')

def mutate_sequence(original_seq):
    """对原始序列进行饱和点突变"""
    mutations = []
    
    # 确保序列长度是3的倍数
    if len(original_seq) % 3 != 0:
        print(f"Warning: Sequence length {len(original_seq)} is not a multiple of 3, may be truncated")
    
    # 将序列分割为密码子
    codons = [original_seq[i:i+3] for i in range(0, len(original_seq)-2, 3)]
    
    for i, codon in enumerate(codons):
        if len(codon) != 3:
            continue  # 跳过不完整的密码子
            
        original_aa = translate_codon(codon)
        position = i + 1  # 密码子位置从1开始
        
        # 检查是否是起始密码子（仅第一个密码子）
        if i == 0 and codon in START_CODONS:
            # 起始密码子保持不变
            mutation_type = f"StartCodon{position}"
            mutated_seq = original_seq
            description = f"Start codon at position {position} remains unchanged"
            
        # 检查是否是终止密码子
        elif codon in STOP_CODONS:
            # 终止密码子保持不变
            mutation_type = f"StopCodon{position}"
            mutated_seq = original_seq
            description = f"Stop codon at position {position} remains unchanged"
            
        else:
            # 根据规则进行突变
            if original_aa != 'A':  # 不是丙氨酸，突变为丙氨酸(GCG)
                mutated_codon = 'GCG'
                mutated_aa = 'A'
                mutation_type = f"{original_aa}{position}A"
                description = f"Position {position}: {codon}({original_aa}) mutated to {mutated_codon}({mutated_aa})"
            else:  # 是丙氨酸，突变为赖氨酸(AAA)
                mutated_codon = 'AAA'
                mutated_aa = 'K'
                mutation_type = f"A{position}K"
                description = f"Position {position}: {codon}({original_aa}) mutated to {mutated_codon}({mutated_aa})"
            
            # 创建突变序列
            mutated_codons = codons.copy()
            mutated_codons[i] = mutated_codon
            mutated_seq = ''.join(mutated_codons)
        
        mutations.append({
            'Mutation_Type': mutation_type,
            'Mutated_Sequence': mutated_seq,
            'Description': description
        })
    
    return mutations

def main():
    # 检查输入文件是否存在
    if not os.path.exists('sequences.xlsx'):
        print("Error: sequences.xlsx file not found")
        return
    
    # 读取Excel文件
    try:
        df = pd.read_excel('sequences.xlsx', header=0)
        print(f"Successfully read file, found {len(df)} sequences")
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    # 确保有足够的列
    if df.shape[1] < 2:
        print("Error: Excel file needs at least 2 columns")
        return
    
    # 处理每条序列
    for index, row in df.iterrows():
        protein_name = str(row.iloc[0])
        dna_sequence = str(row.iloc[1]).upper().replace(' ', '').replace('\n', '')
        
        print(f"Processing protein: {protein_name}, sequence length: {len(dna_sequence)}")
        
        # 生成突变
        mutations = mutate_sequence(dna_sequence)
        
        if not mutations:
            print(f"Warning: No mutations generated for {protein_name}")
            continue
        
        # 创建DataFrame保存结果
        result_df = pd.DataFrame(mutations)
        
        # 保存到Excel文件
        filename = f"{protein_name}_mutations.xlsx"
        try:
            result_df.to_excel(filename, index=False)
            print(f"Saved {len(mutations)} mutations to {filename}")
        except Exception as e:
            print(f"Error saving file {filename}: {e}")

if __name__ == "__main__":
    main()