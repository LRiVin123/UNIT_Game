import random as r
import math as m

class easiy:
    def call(self, p):  # выбор того что даст (+,-,*,:)
        if p == '1':
            return self.plusi()
        elif p == '2':
            return self.minus()
        elif p == '3':
            return self.umnog()
        elif p == '4':
            return self.delit()
        elif p == '5':
            return self.yravn()

    def itog(self, l):
        l = self.xy
        m = r.randint(3, 5)
        c = [l[0]]
        u = [l[0]]
        for i in range(0, 9):
            u_chislo = r.randint(0, 20)
            u_p_or_m = r.randint(0, 2)
            if u_p_or_m == 1:
                u.append(u_chislo)
            else:
                u.append(-u_chislo)
        for i in range(0, m):
            c.append(u[i])
        for i in c:
            if c.count(i) > 1:
                c.remove(i)
        r.shuffle(c)
        return [l[1], l[0], c]

    def plusi(self):
        x = r.randint(0, 9)
        y = r.randint(0, 9)
        self.xy = [x + y, str(x) + "+" + str(y)]
        result = self.itog(self.xy)
        return result

    def minus(self):
        x = r.randint(0, 9)
        y = r.randint(0, 9)
        self.xy = [x - y, str(x) + "-" + str(y)]
        result = self.itog(self.xy)
        return result
    def delit_yr():
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        r.shuffle(x)
        r.shuffle(y)
        for i in y:
            for i1 in x:
                if i1 / i == 0:
                    return i1 / i, i1, i
        return None
    def delit(self): # выражение с делением
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        r.shuffle(x)
        r.shuffle(y)
        for i in y:
            for i1 in x:
                if i1 % i== 0:
                    self.xy = [round(i1 / i), str(i1) + ":" + str(i)]
                    result = self.itog(self.xy)
                    return result
        self.xy = [1, "2:2"]
        result = self.itog(self.xy)
        return result
    def umnog(self): # выражение с умножением
        x = r.randint(0,10)
        y = r.randint(0,10)
        self.xy = [x * y, str(x) + "*" + str(y)]
        result = self.itog(self.xy)
        return result
    def yravn(self):
        lis = "+ " * 9 + "- " * 9 + "* " * 3 + ": " * 3
        c1 = lis.split(" ")
        c1.pop()
        c2 = ""
        y1 = r.randint(0, 20)
        c2 += str(y1)
        r.shuffle(c1)
        t1 = [3, 4, 5, 6, 7, 8, 9]
        r.shuffle(t1)
        for i in range(0, t1[0]):
            if c1[i] == "+" or c1[i] == "-":
                x = r.randint(0, 20)
                if c1[i] == "+":
                    y1 += x
                    c2 += c1[i] + str(x)
                elif c1[i] == "-":
                    y1 -= x
                    c2 += c1[i] + str(x)
            else:
                if c1[i] == ":":
                    div_result = easiy.delit_yr()
                    if div_result is not None:  # Добавляем проверку на None
                        y1 += div_result[0]
                        c2 += "+" + str(div_result[1]) + ":" + str(div_result[2])
                    else:
                        y1 += 1
                        c2 += "+" + '1' + ":" + '1'
                    """
                    div_result_k = 0
                    while div_result_k == 0:

                        if div_result is not None:  # Добавляем проверку на None
                            y1 += div_result[0]
                            c2 += "+" + str(div_result[1]) + ":" + str(div_result[2])
                            div_result_k = 1
                        div_result = easiy.delit_yr()"""

                elif c1[i] == "*":
                    x1 = r.randint(0, 10)
                    x2 = r.randint(0, 10)
                    y1 += x1 * x2
                    c2 += "+" + str(x1) + "*" + str(x2)
        self.xy = [y1, c2]
        result = self.itog(self.xy)
        return result


"""c = "1 "*30+"2 "*29+"3 "*16+"4 "*16+"5 "*9
k = c.split(" ")
k.pop()
while True:
    r.shuffle(k)
    if k[0] < "3" and k[1] < "3" and k[2] < "3" and k[9] > "4":
        break

t = easiy()
for i in range(0,10):
    u=t.call(k[i])
    print(u)
    k3=0
    print(u[2])
    v=u[2]
    for i1 in v:
        k3 = k3 + 1
        print(k3, ")", i1)
        a = int(input())
        if v[a - 1] == u[1]:
           print("yes")
        else:
           print("no")"""

