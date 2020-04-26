
import os
import getpass

os.system("tput setaf 3")

print ("\t\t\tWELCOME TO MULTI TEAM COMPETITION PLATFORM")
os.system("tput setaf 3")
print ("\t\t\t------------------------------------------")

os.system("systemctl start docker")
x=8080
y=1234
users_list=[]
while True:
        print ("""
        Press 1 : to PARTICIPATE
        Press 2 : to JUDGE
        Press 3 : to exit
        """)
        print("Enter your choice : ", end="")
        ch = input()

    
        if int(ch)==1:

                teamID = input("Enter your Team ID : ")
                teamName = input("Enter your Team Name : ")
                user=[]
                volumeName = "myVolume_"+str(x)
                os.system("docker volume create {0}".format(volumeName))
                os.system("docker run -dit --name {0}  -v {1}:/var/www/html  -p {2}:80  centos".format(teamName, volumeName, x))

                #print(os.system("docker inspect --format='{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {0}".format(teamName)))
                #print(str(containerIP))
                user.append(teamID)
                user.append("myVolume_" + str(x))
                user.append(teamName)
                user.append(str(x))
                #user.append("http://"+str(baseIP)+":"+str(x))

                users_list.append(user)
                x=x+1
                y=y+1
        elif int(ch)==2:
                userPassword = getpass.getpass("Enter the password : ")
                originalPassword = "redhat"

                if userPassword != originalPassword:
                        print("Authentication INCORRECT!!!!")
                        exit()

                else :
                        os.system("tput setaf 4")
                        print("\t\t\t\t\t ADMIN DASHBOARD")
                        os.system("tput setaf 4")
                        print("\t\t\t\t\t ---------------")
                        print("""
                        Press 1: to view all the TEAMS
                        Press 2: to remove all existed containers and volumes
                        """)

                        print("Enter your choice : ", end="")
                        ad = input()
                        print (ad)

                        if(int(ad)==1):

                            print("TEAM ID \t\t\t TEAM NAME\t\t\t\tActive Port")
                            for i in range(len (users_list)):
                                print( users_list[i][0]+"\t\t\t\t"+  users_list[i][2]+"\t\t\t\t\t"+ users_list[i][3])

                            print(" Press 0 to get the SYSTEM IP : ", end="")
                            qa=input()
                            if(int(qa)==0):
                                os.system("hostname -I | cut -c1-14")
                            else:
                                print("wrong option, ENTER AGAIN!!!!")


                        elif(int(ad)==2):
                            os.system("docker container stop $(docker container ls -aq)")
                            os.system("docker system prune -f --volumes")
                            os.system("docker container prune -f")
                            print("SUCCESSFULLY DELETED!!!")


        elif int(ch)==3:
                exit()

        else:
                print ("Option doesn't supported")

        
        input("Enter to continue......")
        os.system("clear")

