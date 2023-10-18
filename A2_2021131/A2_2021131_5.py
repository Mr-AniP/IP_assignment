notes_12=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C\'","C#\'","D\'","D#\'","E\'","F\'","F#\'","G\'","G#\'","A\'","A#\'","B\'"]
def noteCreate():
    with open("A2_2021131/scalemajor.txt",'w') as f:
        lines=[]
        for i in range(12):
            line=[]
            line.append(notes_12[i])
            line.append(notes_12[i+2])
            line.append(notes_12[i+4])
            line.append(notes_12[i+5])
            line.append(notes_12[i+7])
            line.append(notes_12[i+9])
            line.append(notes_12[i+11])
            line.append(notes_12[i+12])
            a=" ".join(line) +"\n"
            lines.append(a)
        f.writelines(lines)
    with open("A2_2021131/scaleminor.txt",'w') as f:
        lines=[]
        for i in range(12):
            line=[]
            line.append(notes_12[i])
            line.append(notes_12[i+2])
            line.append(notes_12[i+3])
            line.append(notes_12[i+5])
            line.append(notes_12[i+7])
            line.append(notes_12[i+8])
            line.append(notes_12[i+10])
            line.append(notes_12[i+12])
            a=" ".join(line) +"\n"
            lines.append(a)
        f.writelines(lines)
def majorNotes(Root):
    with open("A2_2021131/scalemajor.txt",'r') as f:
        lines=f.readlines()
        for i in lines:
            l=i.split()
            if l[0]==Root:
                a=len(i)
                print(i[:a-1])
                break
def minorNotes(Root):
    with open("A2_2021131/scaleminor.txt",'r') as f:
        lines=f.readlines()
        for i in lines:
            l=[str(g.strip())for g in i.split()]
            if l[0]==Root:
                a=len(i)
                print(i[:a-1])
                break
noteCreate()
root=input("Enter the root note : ")
scale=input("Enter the type of scale (Major/Minor) : ")
if scale=="Major":
    print("The {} scale in the key of {} is : ".format(scale,root))
    majorNotes(root)
elif scale=="Minor":
    print("The {} scale in the key of {} is : ".format(scale,root))
    minorNotes(root)
else:
    print("Wrong input")
    print("ERROR")