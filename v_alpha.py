# maximum.minimum=int(input("ENter the value of alpha is  - infinity ")),int(input("ENter the value of beta is  + infinity "))
maximum,minimum=1000,-1000
def fun_alphabeta(depth,node,maxplayer,score,alpha,beta):
    if depth==3:
        return score[node]
        
    if maxplayer:
        best=minimum
        for i in range(0,2):
            value=fun_alphabeta(depth+1,node*2+i,False,score,alpha,beta)
            best=max(best,value)
            alpha=max(alpha,best)
            if beta <=alpha:
                break
        return  best
    else:
        best=maximum
        for i in range(0,2):
            value=fun_alphabeta(depth+1,node*2+i,True,score,alpha,beta)
            best=min(best,value)
            beta = min(beta,best)
            if beta<=alpha:
                break
        return best
      
score=[]
x=int(input("ENter the total no of leaf nodes"))
for i in range(x):
    y=int(input("Enter the node value "))
    score.append(y)
      
depth=int(input("Enter the depth value"))
node=int(input("Enter the node value :"))

print("The optimal value is : ",fun_alphabeta(depth,node,True,score,minimum,maximum)
