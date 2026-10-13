from conversores import pes_para_metros

pes = float(input("Digite uma altura em pés: "))

metros = pes_para_metros(pes)

print(f"A altura informada é de: {metros:.2f} metros")