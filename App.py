# main.py

from src.memory_allocator import MemoryAllocator
import random

def transformStrToBits(value: str):
    addresses = value.split(", ")
    return [(int(address)) for address in addresses]

#  nao usar random ou escolehr random com salt
def main():
    # Configurações do sistema de gerenciamento de memória
    print("Configurações do sistema de gerenciamento de memória:")

    virtual_memory_bits =  input("Digite a quantidade de bits para o tamanho da memória virtual: 2^")
    virtual_memory_bits = int(virtual_memory_bits)
    physical_memory_bits = input("Digite a quantidade d bits para o tamanho da memoria fisica: 2^x") # Exemplo: 2^12 para o tamanho da memória física
    physical_memory_bits = int(physical_memory_bits)
    page_size_bits = input("Digite a quantidade de bits para o tamanho da pagina: 2^x")  # Exemplo: 2^8 para o tamanho da página
    page_size_bits = int(page_size_bits)                  

    allocator = MemoryAllocator(virtual_memory_bits, physical_memory_bits, page_size_bits)
    value = input("Digite os endereços virtuais a serem traduzidos: ")
    virtual_addresses = transformStrToBits(value)

    print("Endereço Virtual -> Endereço Físico")
    for va in virtual_addresses:
        try:
            pa = allocator.translate_address(va)
            print(f"{va} -> {pa}")
        except (MemoryError, ValueError) as e:
            print(e)
            break
    
    print("\nTabela de Páginas:")
    page_table = allocator.get_page_table()
    for i, frame in enumerate(page_table):
        if frame != -1:
            print(f"Página {i} -> Moldura {frame}")
    
    print("\nMemória Física (Molduras):")
    physical_memory = allocator.get_physical_memory()
    for i, used in enumerate(physical_memory):
        print(f"Moldura {i}: {'Usada' if used else 'Livre'}")

if __name__ == "__main__":
    main()
