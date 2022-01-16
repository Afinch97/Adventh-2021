import os
from copy import copy
os.chdir(r'C:\Users\antho\Documents\GitHub\Adventh-2021\Day3')
with open('data.txt', 'r') as f:
    lines = f.readlines()
    diagnostics = [entry.strip() for entry in lines]
    oxygen = copy(diagnostics);
    co2 = copy(diagnostics);
    
gamma, epsilon = '',''
for i in range(len(diagnostics[0])):
    all_entries_at_pos = [entry[i] for entry in diagnostics]
    if all_entries_at_pos.count('0') > len(diagnostics)/2:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print('Gamma:', gamma, int(gamma, base=2))
print('Epsilon:', epsilon, int(epsilon, base=2))
print('Power Consumption:', int(epsilon, base=2), '*', int(gamma, base=2), '=', int(gamma, base=2)*int(epsilon, base=2))

for i in range(len(oxygen[0])):
    if len(oxygen) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in oxygen]
    common_bit = '1' if all_entries_at_pos.count('1') >= len(oxygen)/2 else '0'
    oxygen = [entry for entry in oxygen if entry[i]==common_bit]
oxygen_rate = int(oxygen[0], base=2)
print('Oxygen:',oxygen, oxygen_rate)

for i in range(len(co2)):
    if len(co2) == 1:
        break
    all_entries_at_pos = [entry[i] for entry in co2]
    common_bit = '0' if all_entries_at_pos.count('1') >= len(co2)/2 else '1'
    co2 = [entry for entry in co2 if entry[i] == common_bit]
co2_rate = int(co2[0], base=2)
print('Co2:',co2, co2_rate)  

print('Life support rating:', oxygen_rate*co2_rate)  
