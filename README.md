# Numerical-Analysis
The program homework of Numerical Analysis course

## Preview
### 插值法
- [范德蒙德多项式插值](./interp/vandermonde.py)
- [拉格朗日插值法](./interp/lagrange.py)
- [牛顿插值法](./interp/newton.py)
- [分段线性插值](./interp/piece_linear.py)
- [分段三次 Hermite 插值](./interp/hermite.py)  

### 函数逼近
- [最佳平方逼近](./approx/best_square.py)
- [最小二乘法拟合](./approx/least_squares.py)

### 数值积分
- [复合梯形公式](./integration/__init__.py)
- [龙贝格算法](./integration/__init__.py)

### 解线性方程组的直接解法
- [列主元的高斯消元法](./matrix/__init__.py)
- [LU 分解法](./matrix/__init__.py)

### 解线性方程组的迭代解法
- [高斯-塞德尔迭代法](./matrix/__init__.py#L97)
- [SOR 迭代法](./matrix/__init__.py#120)

### 解非线性方程(组)的迭代解法
- [不动点迭代法](./nonlinear/__init__.py#L30)
- [斯蒂芬森迭代法](./nonlinear/__init__.py#L45)
- [牛顿迭代法](./nonlinear/__init__.py#L64)
- [多变量的不动点迭代法](./nonlinear/__init__.py#L79)
- [多变量的牛顿迭代法](./nonlinear/__init__.py#L94)

## Usage
```shell
git clone https://github.com/KuangjuX/Numerical-Analysis.git
pip install -r requirements.txt
python example.py
```
