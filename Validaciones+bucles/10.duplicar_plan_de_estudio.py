# 10) Cursos “Duplicar plan de estudio” — Copia segura
# Como tutor, quiero una función clonar_plan(modulos) que cree una copia independiente de la lista original para probar cambios sin afectar la original.

# Verifica con un cambio en la copia que la original no se altere.
# Usa bucles para mostrar diferencias.

def clonar(modulos):
    copia=modulos.copy()
    return copia

modulos_original=["introduccion","variables","funciones","lista"]
modulos_copia=clonar(modulos_original)

modulos_copia.append("poo")

print("Original")
for i  in modulos_original:
    print(f"- {i}")

print("\nCopia")
for i in modulos_copia:
    print(f"- {i}")

    
