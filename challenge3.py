'''
@Author: Shweta Medhekar
@Created Date: March 2011
'''

import sys

def main():
    txt=open("numbers.csv")
    input_num = txt.readline().rstrip().split(',')
    all_combinations(input_num)
    return
    
def all_combinations(input_num):
    '''Generate all possible sequences'''

    for i in range (0,len(input_num)):
        input_num[i]=int(input_num[i])
    input_num.sort()

    '''Temp storage for the list of numbers'''
    tmp_input=list(input_num)
    final_seq=[] #this is the final list of lists
    counter=0
    
    while(len(tmp_input)>0):
        tmp=[]
        seq=[]        # This is a list which stores
                      # all combinations for a specific set of numbers. 
        tmp.append(tmp_input[0])
        seq.append(tmp)

        for i in range(1,len(tmp_input)):
            for j in range(0,len(seq)):
                tmp=[tmp_input[i]]
                tmp.extend(seq[j])
                seq.append(tmp)

                # Check if tmp is a valid sequence
                total = sum(tmp) 
                for l in range(i+1, len(tmp_input)):
                    if(i<len(tmp_input)-1 and total==tmp_input[l]):
                        print "Condition met : ", tmp, tmp_input[l]
                        counter=counter+1
        final_seq.extend(seq)
        tmp_input.pop(0)

    #print len(final_seq),2**len(input_num)-1#,final_seq
    print "The number of sequences is : ",counter

if __name__ == "__main__":
    sys.exit(main())
