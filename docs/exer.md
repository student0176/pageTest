
**Q:** $S(x)=\sum_{k=0}^{∞} { k+m+1 \choose m+1 }\frac{x^k }{k!}$

**A:**

$S(x)=\sum_{k=0}^{∞} { k+m+1 \choose k }\frac{x^k }{k!} =\sum_{k=0}^{∞} { k+m \choose k-1 }\frac{x^k }{k!} +\sum_{k=0}^{∞} { k+m \choose k }\frac{x^k }{k!}$

$\begin{eqnarray*}
\implies S'(x)&=&\sum_{k=1}^{∞} { k+m \choose k-1 }\frac{x^{k-1 }}{(k-1)!} +\sum_{k=1}^{∞} { k+m \choose k }\frac{x^{k-1 }}{(k-1)!} \\&=&\sum_{k=0}^{∞} { k+m+1 \choose k }\frac{x^{k }}{k!} +\sum_{k=0}^{∞} { k+m+1 \choose k+1 }\frac{x^{k }}{k!}
\\&=&S(x)+\sum_{k=0}^{∞} { k+m+1 \choose k+1 }\frac{x^{k }}{k!}
\end{eqnarray*}$

$\implies S'(x)-S(x)=\sum_{k=0}^{∞} { k+m+1 \choose k+1 }\frac{x^{k }}{k!}$

<br>


${ k+m+1 \choose k+1 }=\frac{(k+m+1)!}{m!(k+1)!} =\frac{(k+m+1)!}{k!(m+1)!}\frac{m+1}{k+1} =\frac{m+1}{k+1} { k+m+1 \choose m+1 }$

$\begin{eqnarray*}
\implies  x(S'(x)-S(x))&=&\sum_{k=0}^{∞}\frac{m+1}{k+1} { k+m+1 \choose m+1 }\frac{x^{k+1 }}{k!}
\\&=&(m+1)\sum_{k=0}^{∞}{ k+m+1 \choose m+1 }\frac{x^{k+1 }}{(k+1)!}
\end{eqnarray*}$

$\implies  [x(S'(x)-S(x))]'=(m+1)\sum_{k=0}^{∞}{ k+m+1 \choose m+1 }\frac{x^{k }}{k!}=(m+1)S(x)$

$\implies x(S''-S')+S'-(m+2)S=0;S(0)=1,S'(0)=m+1$

<br>

some `code` goes here:

```py title="bubble_sort.py" linenums='1' hl_lines='2 3'
for _ in range(10):
    print('hello world')
class Cat:
    def __init__(self):
        self.a = 2
    def forward(self):
        print(self.a)
```


> 这是一个提示[github](https://github.com/student0176/pageTest/)<br>
> 是

士大夫📰

!!! note "a"
    dfe
a

!!! quote "a"
    dfe

!!! warning "a"
    dfe
a

!!! tip "a"
    dfe
a

!!! info "a"
    dfe
a
