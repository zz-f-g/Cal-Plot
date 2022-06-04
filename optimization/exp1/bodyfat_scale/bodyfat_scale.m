close all;
clear;
clc;
load bodyfat_scale.mat;
B = B';
res = RLS(A, B);
[m, n] = size(res);
for k = 1:n
    f(k) = norm(A*res(:,k) - B)^2;
end
f_min = f(:, end);
for k = 1:n
    error(k) = log((f(k) - f_min)/f_min);
end
plot(1:k, error);
