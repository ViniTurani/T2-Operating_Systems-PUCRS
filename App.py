
from src.memoryManager import MemoryManager
import random

# Configurações do sistema de gerenciamento de memória (parametrizáveis)
VIRTUAL_MEMORY_BITS = 16  # Exemplo: 2^16 bits de memória virtual
PHYSICAL_MEMORY_BITS = 12  # Exemplo: 2^12 bits de memória física
PAGE_SIZE_BITS = 8  # Exemplo: 2^8 bits por página

# Criação do objeto MemoryManager
memory_manager = MemoryManager(VIRTUAL_MEMORY_BITS, PHYSICAL_MEMORY_BITS, PAGE_SIZE_BITS)

# Execução da simulação
memory_manager.simulate()

# Exibindo o estado final da memória
print("\nEstado final da tabela de páginas:")
print(memory_manager.page_table)
print("\nEstado final da memória física:")
print(memory_manager.physical_memory)
