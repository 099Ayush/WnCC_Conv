import statistics
import sys

# The function sec(string) returns the total time in seconds from the string of the form "[x]m[y.yyy]s".
# Function tim(total) is the inverse of the function sec(string).
# The algorithm consists of the following steps:
# 1. Declare three lists to store the real, the user and the sys runtimes respectively.
# 2. Read and split each line, and add the sec() of the second slice to the list corres-
#    -ponding to the value of the first slice.
# 3. Display the output according to the desired format, using the 'statistics' module.

def sec(string):
    ret = string.split('m')
    ret[0] = float(ret[0])
    ret[1] = float(ret[1].split('s')[0])
    return ret[1] + ret[0] * 60

def tim(total):
    mn = int(total / 60)
    sc = total - mn * 60
    return str(mn) + 'm' + "%.3f" % sc + 's'  # %.3f to store the seconds with three decimal places.

fin = open(sys.argv[1])
lines = fin.readlines()
t_real = []; t_user = []; t_sys = []

for line in lines: 
    if line == '\n': continue
    ls = line.split()
    if ls[0] == 'real': t_real.append(sec(ls[1]))
    elif ls[0] == 'user': t_user.append(sec(ls[1]))
    elif ls[0] == 'sys': t_sys.append(sec(ls[1]))

def fltr(ls, low, high):
    count = 0
    for l in ls: 
        if (l > low and l < high): count += 1
    return count

m_real = statistics.mean(t_real); sd_real = statistics.stdev(t_real)
m_user = statistics.mean(t_user); sd_user = statistics.stdev(t_user)
m_sys = statistics.mean(t_sys); sd_sys = statistics.stdev(t_sys)

print("Number of runs: %s" % len(t_real))
print("Average Time statistics")
print("real", tim(m_real), "\tuser", tim(m_user), "\tsys", tim(m_sys))
print("Standard deviation of Time statistics")
print("real", tim(sd_real), "\tuser", tim(sd_user), "\tsys", tim(sd_sys))
l_real = m_real - sd_real; h_real = m_real + sd_real
l_user = m_user - sd_user; h_user = m_user + sd_user
l_sys = m_sys - sd_sys; h_sys = m_sys + sd_sys
print("Number of deviations within average - standard deviation to average + standard deviation")
print("real", fltr(t_real, l_real, h_real), "\tuser", fltr(t_user, l_user, h_user), "\tsys", fltr(t_sys, l_sys, h_sys))
