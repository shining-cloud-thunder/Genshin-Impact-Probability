import random
import numpy as np
from colorama import Fore, Back, Style
# 部件和类别
days = input('循环多少天呢？')
for i in range(int(days)):
    print(Fore.RED+'这是第'+str(i+1)+'天结果')
    print()
    for n in range(9):
        leixing = random.choice(['生之花', '死之羽', '时之沙', '空之杯', '理之冠'])
        if leixing == '生之花':
            typedata = [Fore.GREEN+'野花记忆的绿野', Fore.MAGENTA+'远方的少女之心']
            print(random.choice(typedata), '('+leixing+')')
            print('生命值', 717)
            print()
            A = np.array(['攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
            number = random.choice([3, 3, 3, 4])
            if number == 3:
                result3 = np.random.choice(A, 3, replace=False, p=np.array([0.1579, 0.1579, 0.1053, 0.1053, 0.1053, 0.1053, 0.1053, 0.0789, 0.0788]))
                for element in result3:
                    if '攻击力' == element:
                        print('攻击力+', random.choice([14, 16, 18, 19]))
                    elif '防御力' == element:
                        print('防御力+', random.choice([16, 19, 21, 23]))
                    elif '百分比生命值' == element:
                        print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                    elif '百分比攻击力' == element:
                        print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                    elif '百分比防御力' == element:
                        print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                    elif '元素充能效率' == element:
                        print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                    elif '元素精通' == element:
                        print('元素精通+', random.choice(['16', '19', '21', '23']))
                    elif '暴击率' == element:
                        print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                    elif '暴击伤害' == element:
                        print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            else:
                result3 = np.random.choice(A, 4, replace=False, p=np.array([0.1579, 0.1579, 0.1053, 0.1053, 0.1053, 0.1053, 0.1053, 0.0789, 0.0788]))
                for element in result3:
                    if '攻击力' == element:
                        print('攻击力+', random.choice([14, 16, 18, 19]))
                    elif '防御力' == element:
                        print('防御力+', random.choice([16, 19, 21, 23]))
                    elif '百分比生命值' == element:
                        print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                    elif '百分比攻击力' == element:
                        print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                    elif '百分比防御力' == element:
                        print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                    elif '元素充能效率' == element:
                        print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                    elif '元素精通' == element:
                        print('元素精通+', random.choice(['16', '19', '21', '23']))
                    elif '暴击率' == element:
                        print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                    elif '暴击伤害' == element:
                        print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
        elif leixing == '死之羽':
            typedata = [Fore.GREEN+'猎人青翠的箭羽', Fore.MAGENTA+'少女飘摇的思念']
            print(random.choice(typedata), '('+leixing+')')
            print('攻击力:', 42)
            print()
            A = np.array(['生命值', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
            number = random.choice([3, 3, 3, 4])
            if number == 3:
                result3 = np.random.choice(A, 3, replace=False,
                                           p=np.array([0.1579, 0.1579, 0.1053, 0.1053, 0.1053, 0.1053, 0.1053, 0.0789, 0.0788]))
                for element in result3:
                    if '生命值' == element:
                        print('生命值+', random.choice([209, 239, 269, 299]))
                    elif '防御力' == element:
                        print('防御力+', random.choice([16, 19, 21, 23]))
                    elif '百分比生命值' == element:
                        print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                    elif '百分比攻击力' == element:
                        print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                    elif '百分比防御力' == element:
                        print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                    elif '元素充能效率' == element:
                        print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                    elif '元素精通' == element:
                        print('元素精通+', random.choice(['16', '19', '21', '23']))
                    elif '暴击率' == element:
                        print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                    elif '暴击伤害' == element:
                        print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            else:
                result4 = np.random.choice(A, 4, replace=False,
                                           p=np.array([0.1579, 0.1579, 0.1053, 0.1053, 0.1053, 0.1053, 0.1053, 0.0789, 0.0788]))
                for element in result4:
                    if '生命值' == element:
                        print('生命值+', random.choice([209, 239, 269, 299]))
                    elif '防御力' == element:
                        print('防御力+', random.choice([16, 19, 21, 23]))
                    elif '百分比生命值' == element:
                        print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                    elif '百分比攻击力' == element:
                        print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                    elif '百分比防御力' == element:
                        print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                    elif '元素充能效率' == element:
                        print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                    elif '元素精通' == element:
                        print('元素精通+', random.choice(['16', '19', '21', '23']))
                    elif '暴击率' == element:
                        print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                    elif '暴击伤害' == element:
                        print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
        elif leixing == '时之沙':
            typedata = [Fore.GREEN+'翠绿猎人的笃定', Fore.MAGENTA+'少女苦短的良辰']
            print(random.choice(typedata), '('+leixing+')')
            A = np.array(['生命值', '攻击力', '防御力', '元素充能效率', '元素精通'])
            B = np.random.choice(A, replace=False, p=np.array([0.2668, 0.2666, 0.2666, 0.10, 0.10]))
            if B == '生命值':
                print(B + '+7.0%')
                print()
                # A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        # elif '百分比生命值' == element:
                        #     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        # elif '百分比生命值' == element:
                        #     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '攻击力':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比攻击力' == element:
                        #     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比攻击力' == element:
                        #     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '防御力':
                print(B + '+8.7%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比防御力' == element:
                        #     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比防御力' == element:
                        #     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '元素充能效率':
                print(B + '+7.8%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        # elif '元素充能效率' == element:
                        #     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        # elif '元素充能效率' == element:
                        #     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '元素精通':
                print(B + '+28')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        # elif '元素精通' == element:
                        #     print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        # elif '元素精通' == element:
                        #     print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
        elif leixing == '空之杯':
            typedata = [Fore.GREEN+'翠绿猎人的容器', Fore.MAGENTA+'少女片刻的闲暇']
            print(random.choice(typedata), '('+leixing+')')
            A = np.array(['攻击力', '防御力', '生命值', '火元素伤害加成', '雷元素伤害加成', '冰元素伤害加成', '水元素伤害加成', '风元素伤害加成', '岩元素伤害加成', '物理伤害加成', '元素精通'])
            B = np.random.choice(A, replace=False, p=np.array([0.2125, 0.20, 0.2125, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.025]))
            if B == '攻击力':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比攻击力' == element:
                        #     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比攻击力' == element:
                        #     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '防御力':
                print(B + '+8.7%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比防御力' == element:
                        #     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比防御力' == element:
                        #     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '生命值':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        # elif '百分比生命值' == element:
                        #     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        # elif '百分比生命值' == element:
                        #     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '火元素伤害加成':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '雷元素伤害加成':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '冰元素伤害加成':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '水元素伤害加成':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '风元素伤害加成':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '岩元素伤害加成':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '物理伤害加成':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '元素精通':
                print(B + '+28')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        # elif '元素精通' == element:
                        #     print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        # elif '元素精通' == element:
                        #     print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
        elif leixing == '理之冠':
            typedata = [Fore.GREEN+'翠绿的猎人之冠', Fore.MAGENTA+'少女易逝的芳颜']
            print(random.choice(typedata), '('+leixing+')')
            A = np.array(['攻击力', '防御力', '生命值', '暴击率', '暴击伤害', '治疗加成', '元素精通'])
            B = np.random.choice(A, replace=False, p=np.array([0.22, 0.22, 0.22, 0.10, 0.10, 0.10, 0.04]))
            if B == '攻击力':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比攻击力' == element:
                        #     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比攻击力' == element:
                        #     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '防御力':
                print(B + '+8.7%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比防御力' == element:
                        #     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        # elif '百分比防御力' == element:
                        #     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '生命值':
                print(B + '+7.0%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        # elif '百分比生命值' == element:
                        #     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        # elif '百分比生命值' == element:
                        #     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '暴击率':
                print(B + '+4.7%')
                print()
                # A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值','百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1463, 0.1463, 0.1463, 0.0976, 0.0976, 0.0976, 0.0976, 0.0976, 0.0731]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        # elif '暴击率' == element:
                        #     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1463, 0.1463, 0.1463, 0.0976, 0.0976, 0.0976, 0.0976, 0.0976, 0.0731]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        # elif '暴击率' == element:
                        #     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '暴击伤害':
                print(B + '+9.3%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1463, 0.1463, 0.1463, 0.0976, 0.0976, 0.0976, 0.0976, 0.0976, 0.0731]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        # elif '暴击伤害' == element:
                        #     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1463, 0.1463, 0.1463, 0.0976, 0.0976, 0.0976, 0.0976, 0.0976, 0.0731]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        # elif '暴击伤害' == element:
                        #     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '治疗加成':
                print(B + '+5.4%')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '元素精通', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1364, 0.1364, 0.1364, 0.0909, 0.0909, 0.0909, 0.0909, 0.0909, 0.0682, 0.0681]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        elif '元素精通' == element:
                            print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            elif B == '元素精通':
                print(B + '+28')
                print()
                A3 = np.array(['生命值', '攻击力', '防御力', '百分比生命值', '百分比攻击力', '百分比防御力', '元素充能效率', '暴击率', '暴击伤害'])
                number = random.choice([3, 3, 3, 4])
                if number == 3:
                    result3 = np.random.choice(A3, 3, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result3:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        # elif '元素精通' == element:
                        #     print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
                else:
                    result4 = np.random.choice(A3, 4, replace=False,
                                               p=np.array(
                                                   [0.1500, 0.1500, 0.1500, 0.1000, 0.1000, 0.1000, 0.1000, 0.0750, 0.0750]))
                    for element in result4:
                        if '生命值' == element:
                            print('生命值+', random.choice([209, 239, 269, 299]))
                        elif '攻击力' == element:
                            print('攻击力+', random.choice([14, 16, 18, 19]))
                        elif '防御力' == element:
                            print('防御力+', random.choice([16, 19, 21, 23]))
                        elif '百分比生命值' == element:
                            print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比攻击力' == element:
                            print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
                        elif '百分比防御力' == element:
                            print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
                        elif '元素充能效率' == element:
                            print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
                        # elif '元素精通' == element:
                        #     print('元素精通+', random.choice(['16', '19', '21', '23']))
                        elif '暴击率' == element:
                            print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
                        elif '暴击伤害' == element:
                            print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))









            #
            # if '攻击力' in result3:
            #     print('攻击力+', random.choice([14, 16, 18, 19]))
            #     if '防御力' in result3:
            #         print('防御力+', random.choice([16, 19, 21, 23]))
            #         if '百分比生命值' in result3:
            #             print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #             if number == 4:
            #                 if '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '百分比攻击力' in result3:
            #             print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #             if number == 4:
            #                 if '百分比生命值' in result3:
            #                     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '百分比防御力' in result3:
            #             print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #             if number == 4:
            #                 if '百分比生命值' in result3:
            #                     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '元素充能效率' in result3:
            #             print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #             if number == 4:
            #                 if '百分比生命值' in result3:
            #                     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '元素精通' in result3:
            #             print('元素精通+', random.choice(['16', '19', '21', '23']))
            #             if number == 4:
            #                 if '百分比生命值' in result3:
            #                     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '暴击率' in result3:
            #             print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #             if number == 4:
            #                 if '百分比生命值' in result3:
            #                     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '暴击伤害' in result3:
            #             print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #             if number == 4:
            #                 if '百分比生命值' in result3:
            #                     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #     elif '百分比生命值' in result3:
            #         print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         if '防御力' in result3:
            #             print('防御力+', random.choice([16, 19, 21, 23]))
            #             if number == 4:
            #                 if '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '百分比攻击力' in result3:
            #             print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #             if number == 4:
            #                 if '防御力' in result3:
            #                     print('防御力+', random.choice([16, 19, 21, 23]))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '百分比防御力' in result3:
            #             print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #             if number == 4:
            #                 if '防御力' in result3:
            #                     print('防御力+', random.choice([16, 19, 21, 23]))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '元素充能效率' in result3:
            #             print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #             if number == 4:
            #                 if '防御力' in result3:
            #                     print('防御力+', random.choice([16, 19, 21, 23]))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '元素精通' in result3:
            #             print('元素精通+', random.choice(['16', '19', '21', '23']))
            #             if number == 4:
            #                 if '防御力' in result3:
            #                     print('防御力+', random.choice([16, 19, 21, 23]))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '暴击率' in result3:
            #             print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #             if number == 4:
            #                 if '防御力' in result3:
            #                     print('防御力+', random.choice([16, 19, 21, 23]))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击伤害' in result3:
            #                     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         elif '暴击伤害' in result3:
            #             print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #             if number == 4:
            #                 if '防御力' in result3:
            #                     print('防御力+', random.choice([16, 19, 21, 23]))
            #                 elif '百分比攻击力' in result3:
            #                     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #                 elif '百分比防御力' in result3:
            #                     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #                 elif '元素充能效率' in result3:
            #                     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #                 elif '元素精通' in result3:
            #                     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #                 elif '暴击率' in result3:
            #                     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #     elif '百分比攻击力' in result3:
            #         print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         if '防御力' in result3:
            #             print('防御力+', random.choice([16, 19, 21, 23]))
            #         elif '百分比生命值' in result3:
            #             print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比防御力' in result3:
            #             print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #         elif '元素充能效率' in result3:
            #             print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #         elif '元素精通' in result3:
            #             print('元素精通+', random.choice(['16', '19', '21', '23']))
            #         elif '暴击率' in result3:
            #             print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #         elif '暴击伤害' in result3:
            #             print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #     elif '百分比防御力' in result3:
            #         print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #         if '防御力' in result3:
            #             print('防御力+', random.choice([16, 19, 21, 23]))
            #         elif '百分比生命值' in result3:
            #             print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比攻击力' in result3:
            #             print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '元素充能效率' in result3:
            #             print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #         elif '元素精通' in result3:
            #             print('元素精通+', random.choice(['16', '19', '21', '23']))
            #         elif '暴击率' in result3:
            #             print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #         elif '暴击伤害' in result3:
            #             print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #     elif '元素充能效率' in result3:
            #         print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #         if '防御力' in result3:
            #             print('防御力+', random.choice([16, 19, 21, 23]))
            #         elif '百分比生命值' in result3:
            #             print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比攻击力' in result3:
            #             print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比防御力' in result3:
            #             print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #         elif '元素精通' in result3:
            #             print('元素精通+', random.choice(['16', '19', '21', '23']))
            #         elif '暴击率' in result3:
            #             print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #         elif '暴击伤害' in result3:
            #             print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #     elif '元素精通' in result3:
            #         print('元素精通+', random.choice(['16', '19', '21', '23']))
            #         if '防御力' in result3:
            #             print('防御力+', random.choice([16, 19, 21, 23]))
            #         elif '百分比生命值' in result3:
            #             print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比攻击力' in result3:
            #             print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比防御力' in result3:
            #             print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #         elif '元素充能效率' in result3:
            #             print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #         elif '暴击率' in result3:
            #             print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #         elif '暴击伤害' in result3:
            #             print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #     elif '暴击率' in result3:
            #         print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #         if '防御力' in result3:
            #             print('防御力+', random.choice([16, 19, 21, 23]))
            #         elif '百分比生命值' in result3:
            #             print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比攻击力' in result3:
            #             print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比防御力' in result3:
            #             print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #         elif '元素充能效率' in result3:
            #             print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #         elif '元素精通' in result3:
            #             print('元素精通+', random.choice(['16', '19', '21', '23']))
            #         elif '暴击伤害' in result3:
            #             print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #     elif '暴击伤害' in result3:
            #         print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #         if '防御力' in result3:
            #             print('防御力+', random.choice([16, 19, 21, 23]))
            #         elif '百分比生命值' in result3:
            #             print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比攻击力' in result3:
            #             print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #         elif '百分比防御力' in result3:
            #             print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #         elif '元素充能效率' in result3:
            #             print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #         elif '元素精通' in result3:
            #             print('元素精通+', random.choice(['16', '19', '21', '23']))
            #         elif '暴击率' in result3:
            #             print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            # elif '防御力' in result3:
            #     print('防御力+', random.choice([16, 19, 21, 23]))
            #     if '攻击力' in result3:
            #         print('攻击力+', random.choice([14, 16, 18, 19]))
            #     elif '百分比生命值' in result3:
            #         print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比攻击力' in result3:
            #         print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比防御力' in result3:
            #         print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #     elif '元素充能效率' in result3:
            #         print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #     elif '元素精通' in result3:
            #         print('元素精通+', random.choice(['16', '19', '21', '23']))
            #     elif '暴击率' in result3:
            #         print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #     elif '暴击伤害' in result3:
            #         print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            # elif '百分比生命值' in result3:
            #     print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     if '攻击力' in result3:
            #         print('攻击力+', random.choice([14, 16, 18, 19]))
            #     elif '防御力' in result3:
            #         print('防御力+', random.choice([16, 19, 21, 23]))
            #     elif '百分比攻击力' in result3:
            #         print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比防御力' in result3:
            #         print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #     elif '元素充能效率' in result3:
            #         print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #     elif '元素精通' in result3:
            #         print('元素精通+', random.choice(['16', '19', '21', '23']))
            #     elif '暴击率' in result3:
            #         print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #     elif '暴击伤害' in result3:
            #         print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            # elif '百分比攻击力' in result3:
            #     print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     if '攻击力' in result3:
            #         print('攻击力+', random.choice([14, 16, 18, 19]))
            #     elif '防御力' in result3:
            #         print('防御力+', random.choice([16, 19, 21, 23]))
            #     elif '百分比生命值' in result3:
            #         print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比防御力' in result3:
            #         print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #     elif '元素充能效率' in result3:
            #         print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #     elif '元素精通' in result3:
            #         print('元素精通+', random.choice(['16', '19', '21', '23']))
            #     elif '暴击率' in result3:
            #         print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #     elif '暴击伤害' in result3:
            #         print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            # elif '百分比防御力' in result3:
            #     print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #     if '攻击力' in result3:
            #         print('攻击力+', random.choice([14, 16, 18, 19]))
            #     elif '防御力' in result3:
            #         print('防御力+', random.choice([16, 19, 21, 23]))
            #     elif '百分比生命值' in result3:
            #         print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比攻击力' in result3:
            #         print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '元素充能效率' in result3:
            #         print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #     elif '元素精通' in result3:
            #         print('元素精通+', random.choice(['16', '19', '21', '23']))
            #     elif '暴击率' in result3:
            #         print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #     elif '暴击伤害' in result3:
            #         print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            # elif '元素充能效率' in result3:
            #     print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #     if '攻击力' in result3:
            #         print('攻击力+', random.choice([14, 16, 18, 19]))
            #     elif '防御力' in result3:
            #         print('防御力+', random.choice([16, 19, 21, 23]))
            #     elif '百分比生命值' in result3:
            #         print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比攻击力' in result3:
            #         print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比防御力' in result3:
            #         print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #     elif '元素精通' in result3:
            #         print('元素精通+', random.choice(['16', '19', '21', '23']))
            #     elif '暴击率' in result3:
            #         print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #     elif '暴击伤害' in result3:
            #         print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            # elif '元素精通' in result3:
            #     print('元素精通+', random.choice(['16', '19', '21', '23']))
            #     if '攻击力' in result3:
            #         print('攻击力+', random.choice([14, 16, 18, 19]))
            #     elif '防御力' in result3:
            #         print('防御力+', random.choice([16, 19, 21, 23]))
            #     elif '百分比生命值' in result3:
            #         print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比攻击力' in result3:
            #         print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比防御力' in result3:
            #         print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #     elif '元素充能效率' in result3:
            #         print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #     elif '暴击率' in result3:
            #         print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #     elif '暴击伤害' in result3:
            #         print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            # elif '暴击率' in result3:
            #     print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
            #     if '攻击力' in result3:
            #         print('攻击力+', random.choice([14, 16, 18, 19]))
            #     elif '防御力' in result3:
            #         print('防御力+', random.choice([16, 19, 21, 23]))
            #     elif '百分比生命值' in result3:
            #         print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比攻击力' in result3:
            #         print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比防御力' in result3:
            #         print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #     elif '元素充能效率' in result3:
            #         print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #     elif '元素精通' in result3:
            #         print('元素精通+', random.choice(['16', '19', '21', '23']))
            #     elif '暴击伤害' in result3:
            #         print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            # elif '暴击伤害' in result3:
            #     print('暴击伤害+', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
            #     if '攻击力' in result3:
            #         print('攻击力+', random.choice([14, 16, 18, 19]))
            #     elif '防御力' in result3:
            #         print('防御力+', random.choice([16, 19, 21, 23]))
            #     elif '百分比生命值' in result3:
            #         print('生命值+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比攻击力' in result3:
            #         print('攻击力+', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
            #     elif '百分比防御力' in result3:
            #         print('防御力+', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
            #     elif '元素充能效率' in result3:
            #         print('元素充能效率+', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
            #     elif '元素精通' in result3:
            #         print('元素精通+', random.choice(['16', '19', '21', '23']))
            #     elif '暴击率' in result3:
            #         print('暴击率+', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
        print('------------------------')


















# 攻击力:1579
# 防御力:1579
# 百分比生命值:1053
# 百分比攻击力:1053
# 百分比防御力:1053
# 元素充能效率:1053
# 元素精通:1053
# 暴击率:789
# 暴击伤害:789


#print('攻击力:', random.choice([14, 16, 18, 19]))
#print('防御力:', random.choice([16, 19, 21, 23]))
#print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#print('元素精通:', random.choice(['16', '19', '21', '23']))
#print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))




# 生之花副词条

# print(type(result3))
# print(result3[0])
# print(type(result3[0]))




# print('攻击力:', random.choice([14, 16, 18, 19]))
# print('防御力:', random.choice([16, 19, 21, 23]))
# print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
# print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
# print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
# print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
# print('元素精通:', random.choice(['16', '19', '21', '23']))
# print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
# print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))

# if leixing == '生之花':
#     citiaoshu = [3, 3, 3, 4]
#     citiaopanduan = random.choice(citiaoshu)
#     if citiaopanduan == 3:
#         fucitiaotype = {'攻击力':15.79, '防御力':15.79, '百分比生命值':10.53, '百分比攻击力':10.53, '百分比防御力':10.53, '元素充能效率':10.53, '元素精通':10.53, '暴击率':7.89, '暴击伤害':7.89}
#         a = random.randint(0, 10001)
#         if 0 <= a <= 1579:
#             print('攻击力:', random.choice([14, 16, 18, 19]))
#             b = random.randint(0, 10001)
#             if 1580 <= b <= 3158:
#                 print('防御力:', random.choice([16, 19, 21, 23]))
#             elif 3159 <= b <= 4211:
#                 print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 4212 <= b <= 5264:
#                 print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 5265 <= b <= 6317:
#                 print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#             elif 6318 <= b <= 7370:
#                 print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#             elif 7371 <= b <= 8423:
#                 print('元素精通:', random.choice(['16', '19', '21', '23']))
#             elif 8424 <= b <= 9212:
#                 print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#             elif 9213 <= b <= 10001:
#                 print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
#         elif 1580 <= a <= 3158:
#             print('防御力:', random.choice([16, 19, 21, 23]))
#             b = random.randint(0, 10001)
#             if 0 <= b <= 1579:
#                 print('攻击力:', random.choice([14, 16, 18, 19]))
#             elif 3159 <= b <= 4211:
#                 print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 4212 <= b <= 5264:
#                 print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 5265 <= b <= 6317:
#                 print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#             elif 6318 <= b <= 7370:
#                 print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#             elif 7371 <= b <= 8423:
#                 print('元素精通:', random.choice(['16', '19', '21', '23']))
#             elif 8424 <= b <= 9212:
#                 print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#             elif 9213 <= b <= 10001:
#                 print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
#         elif 3159 <= a <= 4211:
#             print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             b = random.randint(0, 10001)
#             if 0 <= b <= 1579:
#                 print('攻击力:', random.choice([14, 16, 18, 19]))
#             elif 1580 <= b <= 3158:
#                 print('防御力:', random.choice([16, 19, 21, 23]))
#             elif 4212 <= b <= 5264:
#                 print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 5265 <= b <= 6317:
#                 print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#             elif 6318 <= b <= 7370:
#                 print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#             elif 7371 <= b <= 8423:
#                 print('元素精通:', random.choice(['16', '19', '21', '23']))
#             elif 8424 <= b <= 9212:
#                 print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#             elif 9213 <= b <= 10001:
#                 print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
#         elif 4212 <= a <= 5264:
#             print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             b = random.randint(0, 10001)
#             if 0 <= b <= 1579:
#                 print('攻击力:', random.choice([14, 16, 18, 19]))
#             elif 1580 <= b <= 3158:
#                 print('防御力:', random.choice([16, 19, 21, 23]))
#             elif 3159 <= b <= 4211:
#                 print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 5265 <= b <= 6317:
#                 print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#             elif 6318 <= b <= 7370:
#                 print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#             elif 7371 <= b <= 8423:
#                 print('元素精通:', random.choice(['16', '19', '21', '23']))
#             elif 8424 <= b <= 9212:
#                 print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#             elif 9213 <= b <= 10001:
#                 print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
#         elif 5265 <= a <= 6317:
#             print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#             b = random.randint(0, 10001)
#             if 0 <= b <= 1579:
#                 print('攻击力:', random.choice([14, 16, 18, 19]))
#             elif 1580 <= b <= 3158:
#                 print('防御力:', random.choice([16, 19, 21, 23]))
#             elif 3159 <= b <= 4211:
#                 print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 4212 <= b <= 5264:
#                 print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 6318 <= b <= 7370:
#                 print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#             elif 7371 <= b <= 8423:
#                 print('元素精通:', random.choice(['16', '19', '21', '23']))
#             elif 8424 <= b <= 9212:
#                 print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#             elif 9213 <= b <= 10001:
#                 print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
#         elif 6318 <= a <= 7370:
#             print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#             b = random.randint(0, 10001)
#             if 0 <= b <= 1579:
#                 print('攻击力:', random.choice([14, 16, 18, 19]))
#             elif 1580 <= b <= 3158:
#                 print('防御力:', random.choice([16, 19, 21, 23]))
#             elif 3159 <= b <= 4211:
#                 print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 4212 <= b <= 5264:
#                 print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 5265 <= b <= 6317:
#                 print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#             elif 7371 <= b <= 8423:
#                 print('元素精通:', random.choice(['16', '19', '21', '23']))
#             elif 8424 <= b <= 9212:
#                 print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#             elif 9213 <= b <= 10001:
#                 print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
#         elif 7371 <= a <= 8423:
#             print('元素精通:', random.choice(['16', '19', '21', '23']))
#             b = random.randint(0, 10001)
#             if 0 <= b <= 1579:
#                 print('攻击力:', random.choice([14, 16, 18, 19]))
#             elif 1580 <= b <= 3158:
#                 print('防御力:', random.choice([16, 19, 21, 23]))
#             elif 3159 <= b <= 4211:
#                 print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 4212 <= b <= 5264:
#                 print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 5265 <= b <= 6317:
#                 print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#             elif 6318 <= b <= 7370:
#                 print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#             elif 8424 <= b <= 9212:
#                 print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#             elif 9213 <= b <= 10001:
#                 print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
#         elif 8424 <= a <= 9212:
#             print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#             b = random.randint(0, 10001)
#             if 0 <= b <= 1579:
#                 print('攻击力:', random.choice([14, 16, 18, 19]))
#             elif 1580 <= b <= 3158:
#                 print('防御力:', random.choice([16, 19, 21, 23]))
#             elif 3159 <= b <= 4211:
#                 print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 4212 <= b <= 5264:
#                 print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 5265 <= b <= 6317:
#                 print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#             elif 6318 <= b <= 7370:
#                 print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#             elif 7371 <= b <= 8423:
#                 print('元素精通:', random.choice(['16', '19', '21', '23']))
#             elif 9213 <= b <= 10001:
#                 print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
#         elif 9213 <= a <= 10001:
#             print('暴击伤害:', random.choice(['5.4%', '6.2%', '7.0%', '7.8%']))
#             b = random.randint(0, 10001)
#             if 0 <= b <= 1579:
#                 print('攻击力:', random.choice([14, 16, 18, 19]))
#             elif 1580 <= b <= 3158:
#                 print('防御力:', random.choice([16, 19, 21, 23]))
#             elif 3159 <= b <= 4211:
#                 print('百分比生命值:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 4212 <= b <= 5264:
#                 print('百分比攻击力:', random.choice(['4.1%', '4.7%', '5.3%', '5.8%']))
#             elif 5265 <= b <= 6317:
#                 print('百分比防御力:', random.choice(['5.1%', '5.8%', '6.6%', '7.3%']))
#             elif 6318 <= b <= 7370:
#                 print('元素充能效率:', random.choice(['4.5%', '5.2%', '5.8%', '6.5%']))
#             elif 7371 <= b <= 8423:
#                 print('元素精通:', random.choice(['16', '19', '21', '23']))
#             elif 8424 <= b <= 9212:
#                 print('暴击率:', random.choice(['2.7%', '3.1%', '3.5%', '3.9%']))
#     elif citiaopanduan == 4:
#         print('no')
#
#
#
#
#











        # b = random.randint(0, 8422)
        # if 0 < b < 1579:

