import numpy as np
import matplotlib.pyplot as plt

k = 8.9875517923e9

def calcular_forca(q1, q2, d):
   
    return k * abs(q1 * q2) / (d ** 2)

def main():
  
    q1 = float(input("Digite o valor da carga q1 (Coulombs): "))
    q2 = float(input("Digite o valor da carga q2 (Coulombs): "))

   
    distancias = np.arange(0.1, 5.0 + 0.1, 0.1)
    forcas = calcular_forca(q1, q2, distancias)

   
    dist_especificas = [0.1, 0.5, 1.0, 2.0, 5.0]

    print("\nForças elétricas para distâncias específicas:")
    for d in dist_especificas:
        f = calcular_forca(q1, q2, d)
        tipo = "Repulsiva" if q1 * q2 > 0 else "Atrativa"
        print(f"d = {d:.1f} m: F = {f:.4e} N ({tipo})")

   
    plt.figure(figsize=(8,5))
    plt.plot(distancias, forcas, label="Força Elétrica (N)", color='blue')
    plt.title("Força Elétrica entre duas cargas em função da distância")
    plt.xlabel("Distância (m)")
    plt.ylabel("Força (N)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
