'''

Dada uma matriz de inteiros nums e um inteiro target, retorne os índices dos dois números de modo que eles somemtarget .

Você pode supor que cada entrada teria exatamente uma solução e não pode usar o mesmo elemento duas vezes.

Você pode retornar a resposta em qualquer ordem.

 

Exemplo 1:

Entrada: nums = [2,7,11,15], target = 9
 Saída: [0,1]
 Explicação: Como nums[0] + nums[1] == 9, retornamos [0, 1].

'''

class Solution(object):
    def twoSum(self,nums,target):
        for i in range(0,len(nums)):
            num1 = nums[i]
            
            if not i == len(nums)-1:
                i += 1
                soma = num1 + nums[i]

                if soma == target:
                    return  [i-1,i]
nums = [2,1,3,7,5]  
target= 12
teste = Solution
print(teste.twoSum(nums,target))