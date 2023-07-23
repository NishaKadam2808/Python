print(".....Welcome to Shopping.....")
s_id=int(input("Choose the Category from Below :- \n\n1.Men\n2.Women\n3.Kids\n\nEnter Category : "))
if(s_id==1 or s_id==2 or s_id==3):
    if(s_id==1):
        print("\n\n......Welcome to Men Section.....")
        m_t=int(input("Choose the Dress Type from Below :- \n\n1.Jeans\n2.Casual\n3.Formal\n4.Sherwani\n\nEnter Dress Type : "))
        if(m_t==1 or m_t==2 or m_t==3 or m_t==4):
            if(m_t==1):
                print("\n\n......Jeans.....")
                m_s=int(input("Choose the Jeans Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                    if(m_s==1):
                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_small_color==1):
                                print("\nCategory : Men\nType : Jeans\nSize : Small\nColour : Black\nPrice : 500")
                            elif(m_small_color==2):
                                print("\nCategory : Men\nType : Jeans\nSize : Small\nColour :White\nPrice : 500")
                            elif(m_small_color==3):
                                print("\nCategory : Men\nType : Jeans\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                            elif(m_small_color==4):
                                print("\nCategory : Men\nType : Jeans\nSize : Small\nColour :Sky Blue\nPrice : 500")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==2):
                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_m_color==1):
                                print("\nCategory : Men\nType : Jeans\nSize : Medium\nColour : Black\nPrice : 600")
                            elif(m_m_color==2):
                                print("\nCategory : Men\nType : Jeans\nSize : Medium\nColour :White\nPrice : 600")
                            elif(m_m_color==3):
                                print("\nCategory : Men\nType : Jeans\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                            elif(m_m_color==4):
                                print("\nCategory : Men\nType : Jeans\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==3):
                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_l_color==1):
                                print("\nCategory : Men\nType : Jeans\nSize : Large\nColour : Black\nPrice : 700")
                            elif(m_l_color==2):
                                print("\nCategory : Men\nType : Jeans\nSize : Large\nColour :White\nPrice : 700")
                            elif(m_l_color==3):
                                print("\nCategory : Men\nType : Jeans\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                            elif(m_l_color==4):
                                print("\nCategory : Men\nType : Jeans\nSize : Large\nColour :Sky Blue\nPrice : 700")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==4):
                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_el_color==1):
                                print("\nCategory : Men\nType : Jeans\nSize : Extra Large\nColour : Black\nPrice : 800")
                            elif(m_el_color==2):
                                print("\nCategory : Men\nType : Jeans\nSize : Extra Large\nColour :White\nPrice : 800")
                            elif(m_el_color==3):
                                print("\nCategory : Men\nType : Jeans\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                            elif(m_el_color==4):
                                print("\nCategory : Men\nType : Jeans\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==5):
                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_del_color==1):
                                print("\nCategory : Men\nType : Jeans\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                            elif(m_del_color==2):
                                print("\nCategory : Men\nType : Jeans\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                            elif(m_del_color==3):
                                print("\nCategory : Men\nType : Jeans\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                            elif(m_del_color==4):
                                print("\nCategory : Men\nType : Jeans\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                        else:
                            print("\nChoose Correct Colour Option....")
                else:
                    print("\nChoose Correct Size Option....")
            if(m_t==2):
                print("\n\n......Casual.....")
                m_s=int(input("Choose the Casual Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                    if(m_s==1):
                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_small_color==1):
                                print("\nCategory : Men\nType : Casual\nSize : Small\nColour : Black\nPrice : 500")
                            elif(m_small_color==2):
                                print("\nCategory : Men\nType : Casual\nSize : Small\nColour :White\nPrice : 500")
                            elif(m_small_color==3):
                                print("\nCategory : Men\nType : Casual\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                            elif(m_small_color==4):
                                print("\nCategory : Men\nType : Casual\nSize : Small\nColour :Sky Blue\nPrice : 500")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==2):
                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_m_color==1):
                                print("\nCategory : Men\nType : Casual\nSize : Medium\nColour : Black\nPrice : 600")
                            elif(m_m_color==2):
                                print("\nCategory : Men\nType : Casual\nSize : Medium\nColour :White\nPrice : 600")
                            elif(m_m_color==3):
                                print("\nCategory : Men\nType : Casual\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                            elif(m_m_color==4):
                                print("\nCategory : Men\nType : Casual\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==3):
                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_l_color==1):
                                print("\nCategory : Men\nType : Casual\nSize : Large\nColour : Black\nPrice : 700")
                            elif(m_l_color==2):
                                print("\nCategory : Men\nType : Casual\nSize : Large\nColour :White\nPrice : 700")
                            elif(m_l_color==3):
                                print("\nCategory : Men\nType : Casual\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                            elif(m_l_color==4):
                                print("\nCategory : Men\nType : Casual\nSize : Large\nColour :Sky Blue\nPrice : 700")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==4):
                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_el_color==1):
                                print("\nCategory : Men\nType : Casual\nSize : Extra Large\nColour : Black\nPrice : 800")
                            elif(m_el_color==2):
                                print("\nCategory : Men\nType : Casual\nSize : Extra Large\nColour :White\nPrice : 800")
                            elif(m_el_color==3):
                                print("\nCategory : Men\nType : Casual\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                            elif(m_el_color==4):
                                print("\nCategory : Men\nType : Casual\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==5):
                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_del_color==1):
                                print("\nCategory : Men\nType : Casual\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                            elif(m_del_color==2):
                                print("\nCategory : Men\nType : Casual\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                            elif(m_del_color==3):
                                print("\nCategory : Men\nType : Casual\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                            elif(m_del_color==4):
                                print("\nCategory : Men\nType : Casual\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                        else:
                            print("\nChoose Correct Colour Option....")
                else:
                    print("\nChoose Correct Size Option....")
            if(m_t==3):
                print("\n\n......Formal.....")
                f_t=int(input("Choose the Type of Formal from Below :- \n\n1.Plain\n2.Checks\n\nEnter Type : "))
                if(f_t==1 or f_t==2):
                    if(f_t==1):
                        m_s=int(input("Choose the Formal Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Men\nType : Formal\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Men\nType : Formal(Plain)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                    if(f_t==2):
                        m_s=int(input("Choose the Formal Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Men\nType : Formal(Checks)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                else:
                    print("Choose Correct Type Option....")
            if(m_t==4):
                print("\n\n......Sherwani.....")
                m_s=int(input("Choose the Casual Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                    if(m_s==1):
                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_small_color==1):
                                print("\nCategory : Men\nType : Sherwani\nSize : Small\nColour : Black\nPrice : 500")
                            elif(m_small_color==2):
                                print("\nCategory : Men\nType : Sherwani\nSize : Small\nColour :White\nPrice : 500")
                            elif(m_small_color==3):
                                print("\nCategory : Men\nType : Sherwani\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                            elif(m_small_color==4):
                                print("\nCategory : Men\nType : Sherwani\nSize : Small\nColour :Sky Blue\nPrice : 500")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==2):
                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_m_color==1):
                                print("\nCategory : Men\nType : Sherwani\nSize : Medium\nColour : Black\nPrice : 600")
                            elif(m_m_color==2):
                                print("\nCategory : Men\nType : Sherwani\nSize : Medium\nColour :White\nPrice : 600")
                            elif(m_m_color==3):
                                print("\nCategory : Men\nType : Sherwani\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                            elif(m_m_color==4):
                                print("\nCategory : Men\nType : Sherwani\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==3):
                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_l_color==1):
                                print("\nCategory : Men\nType : Sherwani\nSize : Large\nColour : Black\nPrice : 700")
                            elif(m_l_color==2):
                                print("\nCategory : Men\nType : Sherwani\nSize : Large\nColour :White\nPrice : 700")
                            elif(m_l_color==3):
                                print("\nCategory : Men\nType : Sherwani\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                            elif(m_l_color==4):
                                print("\nCategory : Men\nType : Sherwani\nSize : Large\nColour :Sky Blue\nPrice : 700")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==4):
                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_el_color==1):
                                print("\nCategory : Men\nType : Sherwani\nSize : Extra Large\nColour : Black\nPrice : 800")
                            elif(m_el_color==2):
                                print("\nCategory : Men\nType : Sherwani\nSize : Extra Large\nColour :White\nPrice : 800")
                            elif(m_el_color==3):
                                print("\nCategory : Men\nType : Sherwani\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                            elif(m_el_color==4):
                                print("\nCategory : Men\nType : Sherwani\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==5):
                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_del_color==1):
                                print("\nCategory : Men\nType : Sherwani\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                            elif(m_del_color==2):
                                print("\nCategory : Men\nType : Sherwani\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                            elif(m_del_color==3):
                                print("\nCategory : Men\nType : Sherwani\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                            elif(m_del_color==4):
                                print("\nCategory : Men\nType : Sherwani\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                        else:
                            print("\nChoose Correct Colour Option....")
                else:
                    print("\nChoose Correct Size Option....")
        else:
            print("\nChoose Correct Type Option....")
    if(s_id==2):
        print("\n\n......Welcome to Women Section.....")
        m_t=int(input("Choose the Dress Type from Below :- \n\n1.Jeans\n2.Crop Top\n3.Formal\n4.Saree\n5.Punjabi\n\nEnter Dress Type : "))
        if(m_t==1 or m_t==2 or m_t==3 or m_t==4 or m_t==5):
            if(m_t==1):
                print("\n\n......Jeans.....")
                m_s=int(input("Choose the Jeans Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                    if(m_s==1):
                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_small_color==1):
                                print("\nCategory : Women\nType : Jeans\nSize : Small\nColour : Black\nPrice : 500")
                            elif(m_small_color==2):
                                print("\nCategory : Women\nType : Jeans\nSize : Small\nColour :White\nPrice : 500")
                            elif(m_small_color==3):
                                print("\nCategory : Women\nType : Jeans\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                            elif(m_small_color==4):
                                print("\nCategory : Women\nType : Jeans\nSize : Small\nColour :Sky Blue\nPrice : 500")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==2):
                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_m_color==1):
                                print("\nCategory : Women\nType : Jeans\nSize : Medium\nColour : Black\nPrice : 600")
                            elif(m_m_color==2):
                                print("\nCategory : Women\nType : Jeans\nSize : Medium\nColour :White\nPrice : 600")
                            elif(m_m_color==3):
                                print("\nCategory : Women\nType : Jeans\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                            elif(m_m_color==4):
                                print("\nCategory : Women\nType : Jeans\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==3):
                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_l_color==1):
                                print("\nCategory : Women\nType : Jeans\nSize : Large\nColour : Black\nPrice : 700")
                            elif(m_l_color==2):
                                print("\nCategory : Women\nType : Jeans\nSize : Large\nColour :White\nPrice : 700")
                            elif(m_l_color==3):
                                print("\nCategory : Women\nType : Jeans\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                            elif(m_l_color==4):
                                print("\nCategory : Women\nType : Jeans\nSize : Large\nColour :Sky Blue\nPrice : 700")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==4):
                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_el_color==1):
                                print("\nCategory : Women\nType : Jeans\nSize : Extra Large\nColour : Black\nPrice : 800")
                            elif(m_el_color==2):
                                print("\nCategory : Women\nType : Jeans\nSize : Extra Large\nColour :White\nPrice : 800")
                            elif(m_el_color==3):
                                print("\nCategory : Women\nType : Jeans\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                            elif(m_el_color==4):
                                print("\nCategory : Women\nType : Jeans\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==5):
                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_del_color==1):
                                print("\nCategory : Women\nType : Jeans\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                            elif(m_del_color==2):
                                print("\nCategory : Women\nType : Jeans\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                            elif(m_del_color==3):
                                print("\nCategory : Women\nType : Jeans\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                            elif(m_del_color==4):
                                print("\nCategory : Women\nType : Jeans\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                        else:
                            print("\nChoose Correct Colour Option....")
                else:
                    print("\nChoose Correct Size Option....")
            if(m_t==2):
                print("\n\n......Crop Top.....")
                m_s=int(input("Choose the Cro Top Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                    if(m_s==1):
                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_small_color==1):
                                print("\nCategory : Women\nType : Crop Top\nSize : Small\nColour : Black\nPrice : 500")
                            elif(m_small_color==2):
                                print("\nCategory : Women\nType : Crop Top\nSize : Small\nColour :White\nPrice : 500")
                            elif(m_small_color==3):
                                print("\nCategory : Women\nType : Crop Top\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                            elif(m_small_color==4):
                                print("\nCategory : Women\nType : Crop Top\nSize : Small\nColour :Sky Blue\nPrice : 500")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==2):
                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_m_color==1):
                                print("\nCategory : Women\nType : Crop Top\nSize : Medium\nColour : Black\nPrice : 600")
                            elif(m_m_color==2):
                                print("\nCategory : Women\nType : Crop Top\nSize : Medium\nColour :White\nPrice : 600")
                            elif(m_m_color==3):
                                print("\nCategory : Women\nType : Crop Top\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                            elif(m_m_color==4):
                                print("\nCategory : Women\nType : Crop Top\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==3):
                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_l_color==1):
                                print("\nCategory : Women\nType : Crop Top\nSize : Large\nColour : Black\nPrice : 700")
                            elif(m_l_color==2):
                                print("\nCategory : Women\nType : Crop Top\nSize : Large\nColour :White\nPrice : 700")
                            elif(m_l_color==3):
                                print("\nCategory : Women\nType : Crop Top\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                            elif(m_l_color==4):
                                print("\nCategory : Women\nType : Crop Top\nSize : Large\nColour :Sky Blue\nPrice : 700")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==4):
                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_el_color==1):
                                print("\nCategory : Women\nType : Crop Top\nSize : Extra Large\nColour : Black\nPrice : 800")
                            elif(m_el_color==2):
                                print("\nCategory : Women\nType : Crop Top\nSize : Extra Large\nColour :White\nPrice : 800")
                            elif(m_el_color==3):
                                print("\nCategory : Women\nType : Crop Top\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                            elif(m_el_color==4):
                                print("\nCategory : Women\nType : Crop Top\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==5):
                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_del_color==1):
                                print("\nCategory : Women\nType : Crop Top\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                            elif(m_del_color==2):
                                print("\nCategory : Women\nType : Crop Top\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                            elif(m_del_color==3):
                                print("\nCategory : Women\nType : Crop Top\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                            elif(m_del_color==4):
                                print("\nCategory : Women\nType : Crop Top\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                        else:
                            print("\nChoose Correct Colour Option....")
                else:
                    print("\nChoose Correct Size Option....")
            if(m_t==3):
                print("\n\n......Formal.....")
                f_t=int(input("Choose the Type of Formal from Below :- \n\n1.Plain\n2.Checks\n\nEnter Type : "))
                if(f_t==1 or f_t==2):
                    if(f_t==1):
                        m_s=int(input("Choose the Formal Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : WomennType : Formal(Plain)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Women\nType : Formal\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Women\nType : Formal(Plain)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                    if(f_t==2):
                        m_s=int(input("Choose the Formal Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : WomennType : Formal(Checks)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Women\nType : Formal(Checks)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                else:
                    print("Choose Correct Type Option....")
            if(m_t==4):
                print("\n\n......Saree.....")
                f_t=int(input("Choose the Type of Saree from Below :- \n\n1.Plain\n2.Checks\n\nEnter Type : "))
                if(f_t==1 or f_t==2):
                    if(f_t==1):
                        m_s=int(input("Choose the Saree Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : WomennType : Saree(Plain)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Women\nType : Saree\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Women\nType : Saree(Plain)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                    if(f_t==2):
                        m_s=int(input("Choose the Saree Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : WomennType : Saree(Checks)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Women\nType : Saree(Checks)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                else:
                    print("Choose Correct Type Option....")
            if(m_t==5):
                print("\n\n......Punjabi.....")
                m_s=int(input("Choose the Punjabi Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                    if(m_s==1):
                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_small_color==1):
                                print("\nCategory : Women\nType : Punjabi\nSize : Small\nColour : Black\nPrice : 500")
                            elif(m_small_color==2):
                                print("\nCategory : Women\nType : Punjabi\nSize : Small\nColour :White\nPrice : 500")
                            elif(m_small_color==3):
                                print("\nCategory : Women\nType : Punjabi\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                            elif(m_small_color==4):
                                print("\nCategory : Women\nType : Punjabi\nSize : Small\nColour :Sky Blue\nPrice : 500")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==2):
                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_m_color==1):
                                print("\nCategory : Women\nType : Punjabi\nSize : Medium\nColour : Black\nPrice : 600")
                            elif(m_m_color==2):
                                print("\nCategory : Women\nType : Punjabi\nSize : Medium\nColour :White\nPrice : 600")
                            elif(m_m_color==3):
                                print("\nCategory : Women\nType : Punjabi\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                            elif(m_m_color==4):
                                print("\nCategory : Women\nType : Punjabi\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==3):
                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_l_color==1):
                                print("\nCategory : Women\nType : Punjabi\nSize : Large\nColour : Black\nPrice : 700")
                            elif(m_l_color==2):
                                print("\nCategory : Women\nType : Punjabi\nSize : Large\nColour :White\nPrice : 700")
                            elif(m_l_color==3):
                                print("\nCategory : Women\nType : Punjabi\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                            elif(m_l_color==4):
                                print("\nCategory : Women\nType : Punjabi\nSize : Large\nColour :Sky Blue\nPrice : 700")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==4):
                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_el_color==1):
                                print("\nCategory : Women\nType : Punjabi\nSize : Extra Large\nColour : Black\nPrice : 800")
                            elif(m_el_color==2):
                                print("\nCategory : Women\nType : Punjabi\nSize : Extra Large\nColour :White\nPrice : 800")
                            elif(m_el_color==3):
                                print("\nCategory : Women\nType : Punjabi\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                            elif(m_el_color==4):
                                print("\nCategory : Women\nType : Punjabi\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                        else:
                            print("\nChoose Correct Colour Option....")
                    if(m_s==5):
                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                            print("\n\n.....Your Order is Successfully Placed.....")
                            print("\n.............................................")
                            print("\n\nOrder Details :")
                            if(m_del_color==1):
                                print("\nCategory : Women\nType : Punjabi\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                            elif(m_del_color==2):
                                print("\nCategory : Women\nType : Punjabi\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                            elif(m_del_color==3):
                                print("\nCategory : Women\nType : Punjabi\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                            elif(m_del_color==4):
                                print("\nCategory : Women\nType : Punjabi\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                        else:
                            print("\nChoose Correct Colour Option....")
                else:
                    print("\nChoose Correct Size Option....")
        else:
            print("\nChoose Correct Type Option....")
    if(s_id==3):
        print("\n\n......Welcome to Kids Section.....")
        k_g=int(input("Choose the Gender of your Kid :- \n\n1.Girl\n2.Boy\n\nEnter Gender : "))
        if(k_g==1 or k_g==2):
            if(k_g==1):
                m_t=int(input("Choose the Type of Dress:- \n\n1.Jeans\n2.Crop Top\n3.Skirt\n4.Jumpsuit\n\nEnter Dress Type : "))
                if(m_t==1 or m_t==2 or m_t==3 or m_t==4):
                    if(m_t==1):
                        print("\n\n......Jeans.....")
                        m_s=int(input("Choose the Jeans Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Jeans\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                    if(m_t==2):
                        print("\n\n......Crop Top.....")
                        m_s=int(input("Choose the Crop Top Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Kids(Girl)\nType : Crop Top\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                    if(m_t==3):
                        print("\n\n......Skirt.....")
                        f_t=int(input("Choose the Type of Skirt from Below :- \n\n1.Plain\n2.Checks\n\nEnter Type : "))
                        if(f_t==1 or f_t==2):
                            if(f_t==1):
                                m_s=int(input("Choose the Skirt Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                                    if(m_s==1):
                                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_small_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Small\nColour : Black\nPrice : 500")
                                            elif(m_small_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Small\nColour :White\nPrice : 500")
                                            elif(m_small_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                            elif(m_small_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==2):
                                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_m_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Medium\nColour : Black\nPrice : 600")
                                            elif(m_m_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Medium\nColour :White\nPrice : 600")
                                            elif(m_m_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                            elif(m_m_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==3):
                                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_l_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Large\nColour : Black\nPrice : 700")
                                            elif(m_l_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Large\nColour :White\nPrice : 700")
                                            elif(m_l_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                            elif(m_l_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==4):
                                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_el_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                            elif(m_el_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Extra Large\nColour :White\nPrice : 800")
                                            elif(m_el_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                            elif(m_el_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==5):
                                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_del_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                            elif(m_del_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                            elif(m_del_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                            elif(m_del_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Plain)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                else:
                                    print("\nChoose Correct Size Option....")
                            if(f_t==2):
                                m_s=int(input("Choose the Formal Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                                    if(m_s==1):
                                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_small_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Small\nColour : Black\nPrice : 500")
                                            elif(m_small_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Small\nColour :White\nPrice : 500")
                                            elif(m_small_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                            elif(m_small_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==2):
                                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_m_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Medium\nColour : Black\nPrice : 600")
                                            elif(m_m_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Medium\nColour :White\nPrice : 600")
                                            elif(m_m_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                            elif(m_m_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==3):
                                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_l_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Large\nColour : Black\nPrice : 700")
                                            elif(m_l_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Large\nColour :White\nPrice : 700")
                                            elif(m_l_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                            elif(m_l_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==4):
                                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_el_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                            elif(m_el_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Extra Large\nColour :White\nPrice : 800")
                                            elif(m_el_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                            elif(m_el_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==5):
                                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_del_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                            elif(m_del_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                            elif(m_del_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                            elif(m_del_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Skirt(Checks)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                else:
                                    print("\nChoose Correct Size Option....")
                        else:
                            print("Choose Correct Type Option....")
                    if(m_t==4):
                        print("\n\n......Jumpsuit.....")
                        f_t=int(input("Choose the Type of Jumpsuit from Below :- \n\n1.Plain\n2.Checks\n\nEnter Type : "))
                        if(f_t==1 or f_t==2):
                            if(f_t==1):
                                m_s=int(input("Choose the Jumpsuit Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                                    if(m_s==1):
                                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_small_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Small\nColour : Black\nPrice : 500")
                                            elif(m_small_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Small\nColour :White\nPrice : 500")
                                            elif(m_small_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                            elif(m_small_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==2):
                                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_m_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Medium\nColour : Black\nPrice : 600")
                                            elif(m_m_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Medium\nColour :White\nPrice : 600")
                                            elif(m_m_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                            elif(m_m_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==3):
                                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_l_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Large\nColour : Black\nPrice : 700")
                                            elif(m_l_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Large\nColour :White\nPrice : 700")
                                            elif(m_l_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                            elif(m_l_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==4):
                                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_el_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                            elif(m_el_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Extra Large\nColour :White\nPrice : 800")
                                            elif(m_el_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                            elif(m_el_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==5):
                                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_del_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                            elif(m_del_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                            elif(m_del_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                            elif(m_del_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Plain)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                else:
                                    print("\nChoose Correct Size Option....")
                            if(f_t==2):
                                m_s=int(input("Choose the Jumpsuit Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                                if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                                    if(m_s==1):
                                        m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_small_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Small\nColour : Black\nPrice : 500")
                                            elif(m_small_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Small\nColour :White\nPrice : 500")
                                            elif(m_small_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                            elif(m_small_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==2):
                                        m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_m_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Medium\nColour : Black\nPrice : 600")
                                            elif(m_m_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Medium\nColour :White\nPrice : 600")
                                            elif(m_m_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                            elif(m_m_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==3):
                                        m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_l_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Large\nColour :White\nPrice : 700")
                                            elif(m_l_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                            elif(m_l_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==4):
                                        m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_el_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Extra Large\nColour : Black\nPrice : 800")
                                            elif(m_el_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Extra Large\nColour :White\nPrice : 800")
                                            elif(m_el_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                            elif(m_el_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                    if(m_s==5):
                                        m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                        if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                            print("\n\n.....Your Order is Successfully Placed.....")
                                            print("\n.............................................")
                                            print("\n\nOrder Details :")
                                            if(m_del_color==1):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                            elif(m_del_color==2):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                            elif(m_del_color==3):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                            elif(m_del_color==4):
                                                print("\nCategory : Kids(Girl)\nType : Jumpsuit(Checks)\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                        else:
                                            print("\nChoose Correct Colour Option....")
                                else:
                                    print("\nChoose Correct Size Option....")
                        else:
                            print("Choose Correct Type Option....")
                else:
                    print("\nChoose Correct Type Option....")
            if(k_g==2):
                m_t=int(input("Choose the Type of Dress:- \n\n1.Jeans\n2.T-Shirt\n3.Sherwani\n\nEnter Dress Type : "))
                if(m_t==1 or m_t==2 or m_t==3 or m_t==4):
                    if(m_t==1):
                        print("\n\n......Jeans.....")
                        m_s=int(input("Choose the Jeans Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Jeans\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                    if(m_t==2):
                        print("\n\n......T-Shirt.....")
                        m_s=int(input("Choose the Crop Top Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Kids(Boy)\nType : T-Shirt\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                    if(m_t==3):
                        print("\n\n......Sherwani.....")
                        m_s=int(input("Choose the Casual Size from Below :- \n\n1.Small(S)\n2.Medium(M)\n3.Large(L)\n4.Extra Large(XL)\n5.Double Extra Large(XXL)\n\nEnter Size : "))
                        if(m_s==1 or m_s==2 or m_s==3 or m_s==4 or m_s==5):
                            if(m_s==1):
                                m_small_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_small_color==1 or m_small_color==2 or m_small_color==3 or m_small_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_small_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Small\nColour : Black\nPrice : 500")
                                    elif(m_small_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Small\nColour :White\nPrice : 500")
                                    elif(m_small_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Small\nColour :Nevy Blue\nPrice : 500")
                                    elif(m_small_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Small\nColour :Sky Blue\nPrice : 500")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==2):
                                m_m_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_m_color==1 or m_m_color==2 or m_m_color==3 or m_m_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_m_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Medium\nColour : Black\nPrice : 600")
                                    elif(m_m_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Medium\nColour :White\nPrice : 600")
                                    elif(m_m_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Medium\nColour :Nevy Blue\nPrice : 600")
                                    elif(m_m_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Medium\nColour :Sky Blue\nPrice : 600")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==3):
                                m_l_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_l_color==1 or m_l_color==2 or m_l_color==3 or m_l_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_l_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Large\nColour : Black\nPrice : 700")
                                    elif(m_l_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Large\nColour :White\nPrice : 700")
                                    elif(m_l_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Large\nColour :Nevy Blue\nPrice : 700")
                                    elif(m_l_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Large\nColour :Sky Blue\nPrice : 700")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==4):
                                m_el_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_el_color==1 or m_el_color==2 or m_el_color==3 or m_el_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_el_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Extra Large\nColour : Black\nPrice : 800")
                                    elif(m_el_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Extra Large\nColour :White\nPrice : 800")
                                    elif(m_el_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Extra Large\nColour :Nevy Blue\nPrice : 800")
                                    elif(m_el_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Extra Large\nColour :Sky Blue\nPrice : 800")
                                else:
                                    print("\nChoose Correct Colour Option....")
                            if(m_s==5):
                                m_del_color=int(input("\nChoose Colour from Below :-\n\n1.Black\n2.White\n3.Nevy Blue\n4.Sky Blue\n\nEnter Colour : "))
                                if(m_del_color==1 or m_del_color==2 or m_del_color==3 or m_del_color==4):
                                    print("\n\n.....Your Order is Successfully Placed.....")
                                    print("\n.............................................")
                                    print("\n\nOrder Details :")
                                    if(m_del_color==1):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Double Extra Large\nColour : Black\nPrice : 1000")
                                    elif(m_del_color==2):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Double Extra Large\nColour :White\nPrice : 1000")
                                    elif(m_del_color==3):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Double Extra Large\nColour :Nevy Blue\nPrice : 1000")
                                    elif(m_del_color==4):
                                        print("\nCategory : Kids(Boy)\nType : Sherwani\nSize : Double Extra Large\nColour :Sky Blue\nPrice : 1000")
                                else:
                                    print("\nChoose Correct Colour Option....")
                        else:
                            print("\nChoose Correct Size Option....")
                else:
                    print("\nChoose Correct Type Option....")
        else:
            print("\nChoose Correct Gender Option....")
else:
    print("\nChoose Correct Category Option....")
        
                    
                        
