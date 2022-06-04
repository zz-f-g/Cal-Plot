function res = RLS(A,b)
%solve Ax = b using recursive least square.
format long;
[m,n] = size(A);
% initialize;
x = rand(n,1);
I = eye(n,n);
P = (10^6) * I;
% recursion
for k = 1:m
    Ak = A(k,:);
    K = P*(Ak')/(1 + Ak*P*Ak');
    x = x + K * (b(k) - Ak * x);
    P = (I - K*Ak) * P;
    thetae(:,k) = x;
end
% return log
res = thetae;
end
