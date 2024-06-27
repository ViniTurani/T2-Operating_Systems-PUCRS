# main.py

from src.memory_allocator import MemoryAllocator
import random

def generate_virtual_addresses(num_addresses, virtual_memory_bits):
    return [random.randint(0, 2**virtual_memory_bits - 1) for _ in range(num_addresses)]
#  nao usar random ou escolehr random com salt
def main():
    # Configurações do sistema de gerenciamento de memória
    virtual_memory_bits = 16  # Exemplo: 2^16 para o tamanho da memória virtual
    physical_memory_bits = 12  # Exemplo: 2^12 para o tamanho da memória física
    page_size_bits = 8  # Exemplo: 2^8 para o tamanho da página
    #  input 
    allocator = MemoryAllocator(virtual_memory_bits, physical_memory_bits, page_size_bits)
    num_virtual_addresses = 10
    virtual_addresses = generate_virtual_addresses(num_virtual_addresses, virtual_memory_bits)
    
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
