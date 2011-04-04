'''
@Description: Find the longest palindrome
@Author: Shweta Medhekar
@Created Date: March 2011
'''

import sys

def find_palindrome():
    a='FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'

    palindrome=''

    for i in range(0,len(a)):
        #to find 'odd' palindrome of the type abcba
        j=1
        while ((i-j)>=0 and (i+j)<len(a) and a[i-j]==a[i+j]):
            j=j+1

        current=a[(i-j+1):(i+j)]
        if(len(current)>len(palindrome)):
            palindrome=current

        #to find 'even' palindromes of the type abba
        j=0
        while ((i-j)>=0 and (i+1+j)<len(a) and a[i-j]==a[i+1+j]): 
            j=j+1

        current=a[(i-j+1):(i+j+1)]
        if(len(current)>len(palindrome)):
            palindrome=current

    print "palindrome is : ",palindrome
        
        
if __name__ == "__main__":
    sys.exit(find_palindrome())
    

