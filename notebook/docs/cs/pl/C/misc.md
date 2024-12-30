# Misc

!!! abstract 
    收录一些自己没想到的写法

## 一、涉及数字比较的写法

>From PTA, 年份大小比较

```c
int cmp(int b1, int b2) {
    int y1 = b1 / 10000; // 年份
    int m1 = (b1 % 10000) / 100; // 月份
    int d1 = b1 % 100; // 日

    int y2 = b2 / 10000; // 年份
    int m2 = (b2 % 10000) / 100; // 月份
    int d2 = b2 % 100; // 日

    if (y1 != y2) {
        return y1 < y2 ? 1 : 0;
    }
    if (m1 != m2) {
        return m1 < m2 ? 1 : 0;
    }
    return d1 < d2 ? 1 : 0;
}
```