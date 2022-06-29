# # z = "a b c d e f g h"
# # d = "A B C D E F G H"
# # g = "1 2 3 4 5 "
# # i = "! @ # "

# It's first approach.

# # a = z.split()
# # b = d.split()
# # c = g.split()
# # e = i.split()
# # print('''lower=a,b,c,d,e,f,g,h
# # upper = A,B,C,D,E,F,G,H
# # num  =  1,2,3,4,5
# # sp char=!,@,#''')
# # print("choose 8 char")
# # l = input("enter the password:")
# # if len(l)<8 :
# #     print("it should be 8 characters")
# # elif len(l)==8:
# #     print("level 1 cleared.....")
# #     if a[0]==l[0] or a[0]==l[1] or a[0]==l[2] or a[0]==l[3] or a[0]==l[4] or a[0]==l[5] or a[0]==l[7] or a[1]==l[0] or a[1]==l[1] or a[1]==l[2] or a[1]==l[3] or a[1]==l[4] or a[1]==l[5] or a[1]==l[7] or a[2]==l[0] or a[2]==l[1] or a[2]==l[2] or a[2]==l[3] or a[2]==l[4] or a[2]==l[5] or a[2]==l[7] or a[3]==l[0] or a[3]==l[1] or a[3]==l[2] or a[3]==l[3] or a[3]==l[4] or a[3]==l[5] or a[3]==l[7] or a[4]==l[0] or a[4]==l[1] or a[4]==l[2] or a[4]==l[3] or a[4]==l[4] or a[4]==l[5] or a[4]==l[7] or a[5]==l[0] or a[5]==l[1] or a[5]==l[2] or a[5]==l[3] or a[5]==l[4] or a[5]==l[5] or a[5]==l[7] or a[6]==l[0] or a[6]==l[1] or a[6]==l[2] or a[6]==l[3] or a[6]==l[4] or a[6]==l[5] or a[6]==l[7] or a[7]==l[0] or a[7]==l[1] or a[7]==l[2] or a[7]==l[3] or a[7]==l[4] or a[7]==l[5] or a[7]==l[7]:
# #         print("level 2 cleared......")
# #         if b[0]==l[0] or b[0]==b[1] or b[0]==l[2] or b[0]==l[3] or b[0]==l[4] or b[0]==l[5] or b[0]==l[7] or b[1]==l[0] or b[1]==l[1] or b[1]==l[2] or b[1]==l[3] or b[1]==l[4] or b[1]==l[5] or b[1]==l[7] or b[2]==l[0] or b[2]==l[1] or b[2]==l[2] or b[2]==l[3] or b[2]==l[4] or b[2]==l[5] or b[2]==l[7] or b[3]==l[0] or b[3]==l[1] or b[3]==l[2] or b[3]==l[3] or b[3]==l[4] or b[3]==l[5] or b[3]==l[7] or b[4]==l[0] or b[4]==l[1] or b[4]==l[2] or b[4]==l[3] or b[4]==l[4] or b[4]==l[5] or b[4]==l[7] or b[5]==l[0] or b[5]==l[1] or b[5]==l[2] or b[5]==l[3] or b[5]==l[4] or b[5]==l[5] or b[5]==l[7] or b[6]==l[0] or b[6]==l[1] or b[6]==l[2] or b[6]==l[3] or b[6]==l[4] or b[6]==l[5] or b[6]==l[7] or b[7]==l[0] or b[7]==l[1] or b[7]==l[2] or b[7]==l[3] or b[7]==l[4] or b[7]==l[5] or b[7]==l[7]:
# #             print("level 3 cleared.....")
# #             if l[0]==c[0] or l[0]==c[1] or l[0] == c[2] or l[0] == c[3] or l[0] == c[4] or l[1]==c[0] or l[1]==c[1] or l[1] == c[2] or l[1] == c[3] or l[1] == c[4] or l[2]==c[0] or l[2]==c[1] or l[2] == c[2] or l[2] == c[3] or l[2] == c[4] or l[4]==c[0] or l[4]==c[1] or l[4] == c[2] or l[4] == c[3] or l[4] == c[4] or l[5]==c[0] or l[5]==c[1] or l[5] == c[2] or l[5] == c[3] or l[5] == c[4] or l[6]==c[0] or l[6]==c[1] or l[6] == c[2] or l[6] == c[3] or l[6] == c[4] or l[7]==c[0] or l[7]==c[1] or l[7] == c[2] or l[7] == c[3] or l[7] == c[4] :
# #                 print("level 3 cleared.......")
# #                 if l[0]==e[0] or l[0]==e[1] or l[0]==e[2] or l[1]==e[0] or l[1]==e[1] or l[1]==e[2] or l[2]==e[0] or l[2]==e[1] or l[2]==e[2] or l[3]==e[0] or l[3]==e[1] or l[3]==e[2] or l[4]==e[0] or l[4]==e[1] or l[4]==e[2] or l[5]==e[0] or l[5]==e[1] or l[5]==e[2] or l[6]==e[0] or l[6]==e[1] or l[6]==e[2] or l[7]==e[0] or l[7]==e[1] or l[7]==e[2] :
# #                     print("processes completed/-")
# #                     print("your password is strong..")
# #                 else:
# #                     print("more than average password....")
# #             else:
# #                 print("normal password....")
# #         else:
# #             print("weak password....")
# #     else:
# #         print("very weak password...")
        
# # else:
# #     print("it should be of 8 letters")


# It's second approach.

# d = "@ # $"
# e = d.split()
# z = input("enter the password:")
# if len(z)==8:
#     if z[0].isupper()== True or z[1].isupper()== True or z[2].isupper()== True or z[3].isupper()== True or z[4].isupper()== True or z[5].isupper()== True or z[6].isupper()== True or z[7].isupper()== True:
#         print("level 1 check cleared.....")
#         if z[0].islower()== True or z[1].islower()== True or z[2].islower()== True or z[3].islower()== True or z[4].islower()== True or z[5].islower()== True or z[6].islower()== True or z[7].islower()== True:
#             print("level 2 check cleared.......")
#             if z[0].isnumeric()== True or z[1].isnumeric()== True or z[2].isnumeric()== True or z[3].isnumeric()== True or z[4].isnumeric()== True or z[5].isnumeric()== True or z[6].isnumeric()== True or z[7].isnumeric()== True:
#                 print("numeric level cleared.......")
#                 if z[0]==e[0] or z[0]==e[1] or z[0]==e[2] or z[1]==e[0] or z[1]==e[1] or z[1]==e[2] or z[2]==e[0] or z[2]==e[1] or z[2]==e[2] or z[3]==e[0] or z[3]==e[1] or z[3]==e[2] or z[4]==e[0] or z[4]==e[1] or z[4]==e[2] or z[5]==e[0] or z[5]==e[1] or z[5]==e[2] or z[6]==e[0] or z[6]==e[1] or z[6]==e[2] or z[7]==e[0] or z[7]==e[1] or z[7]==e[2] :
#                     print("final level cleared...")
#                     print("congrats this is a strong password....")
#                 else:
#                     print("average password.")
#             else:
#                 print("below average password.")
#         else:
#             print("weak password.")
#     else:
#         print("super weak password.")
# else:
#     print("password should be of 8 characters")
