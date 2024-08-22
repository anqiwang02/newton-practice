{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "b53b8cc0-a14a-4cb2-b38d-73d86eea6bc5",
   "metadata": {},
   "outputs": [
    {
     "ename": "RecursionError",
     "evalue": "maximum recursion depth exceeded",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mRecursionError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[8], line 9\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m (d_fun(x\u001b[38;5;241m+\u001b[39mh)\u001b[38;5;241m-\u001b[39md_fun(x))\u001b[38;5;241m/\u001b[39mh \u001b[38;5;66;03m#derivative of fun(x)\u001b[39;00m\n\u001b[1;32m      8\u001b[0m f\u001b[38;5;241m=\u001b[39mx0\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m2\u001b[39m\n\u001b[0;32m----> 9\u001b[0m df\u001b[38;5;241m=\u001b[39m\u001b[43md_fun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mx0\u001b[49m\u001b[43m)\u001b[49m\n",
      "Cell \u001b[0;32mIn[8], line 6\u001b[0m, in \u001b[0;36md_fun\u001b[0;34m(x)\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21md_fun\u001b[39m(x):\n\u001b[1;32m      5\u001b[0m     h\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m10\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39m(\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m5\u001b[39m)\n\u001b[0;32m----> 6\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m (\u001b[43md_fun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mx\u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43mh\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241m-\u001b[39md_fun(x))\u001b[38;5;241m/\u001b[39mh\n",
      "Cell \u001b[0;32mIn[8], line 6\u001b[0m, in \u001b[0;36md_fun\u001b[0;34m(x)\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21md_fun\u001b[39m(x):\n\u001b[1;32m      5\u001b[0m     h\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m10\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39m(\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m5\u001b[39m)\n\u001b[0;32m----> 6\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m (\u001b[43md_fun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mx\u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43mh\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241m-\u001b[39md_fun(x))\u001b[38;5;241m/\u001b[39mh\n",
      "    \u001b[0;31m[... skipping similar frames: d_fun at line 6 (2971 times)]\u001b[0m\n",
      "Cell \u001b[0;32mIn[8], line 6\u001b[0m, in \u001b[0;36md_fun\u001b[0;34m(x)\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21md_fun\u001b[39m(x):\n\u001b[1;32m      5\u001b[0m     h\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m10\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39m(\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m5\u001b[39m)\n\u001b[0;32m----> 6\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m (\u001b[43md_fun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mx\u001b[49m\u001b[38;5;241;43m+\u001b[39;49m\u001b[43mh\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241m-\u001b[39md_fun(x))\u001b[38;5;241m/\u001b[39mh\n",
      "\u001b[0;31mRecursionError\u001b[0m: maximum recursion depth exceeded"
     ]
    }
   ],
   "source": [
    "import math\n",
    "x0=1\n",
    "\n",
    "def d_fun(x):\n",
    "    h=10**(-5)\n",
    "    return (d_fun(x+h)-d_fun(x))/h #derivative of fun(x)\n",
    "\n",
    "f=x0**2\n",
    "df=d_fun(x0)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7b06a1bb-59b6-4040-a0a4-4989af6f975f",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1298438422.py, line 15)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[1], line 15\u001b[0;36m\u001b[0m\n\u001b[0;31m    epi=1*10^^-5\u001b[0m\n\u001b[0m             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "x0=1\n",
    "\n",
    "f=x**2\n",
    "df=diff(f)\n",
    "ddf=diff(df)\n",
    "print(df)\n",
    "print(ddf)\n",
    "\n",
    "\n",
    "\n",
    "    \n",
    "def d_fun(x):\n",
    "    epi=1*10^^-5\n",
    "    return (d_fun(x+h)-d_fun(x))/h #derivative of fun(x)\n",
    "\n",
    "def d2_fun(x):\n",
    "    \n",
    "\n",
    "x_0 #same as x_t-1\n",
    "x_1 #same as x_t\n",
    "def newton()\n",
    "if math.abs(x0-x1)=0:\n",
    "    break"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
