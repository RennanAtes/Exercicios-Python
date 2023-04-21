'''

Dada uma matriz de inteiros nums e um inteiro target, retorne os índices dos dois números de modo que eles somemtarget .

Você pode supor que cada entrada teria exatamente uma solução e não pode usar o mesmo elemento duas vezes.

Você pode retornar a resposta em qualquer ordem.

 

Exemplo 1:

Entrada: nums = [2,7,11,15], target = 9
 Saída: [0,1]
 Explicação: Como nums[0] + nums[1] == 9, retornamos [0, 1].

'''


                
nums = [3,2,3]  
target= 6


class Solution(object):
    def twoSum(nums,target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
teste = Solution
print(teste.twoSum(nums,target))