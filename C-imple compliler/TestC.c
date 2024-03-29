int main(){
	L_1: 
	L_3: temp= num;
	 L_4: if (temp>0) goto L_6;
	L_5: goto L_15; 
	L_6: T_1=temp/10; 
	L_7: digit= T_1;
	 L_8: T_2=digit*digit; 
	L_9: T_3=T_2*digit; 
	L_10: T_4=sum+T_3; 
	L_11: sum= T_4;
	 L_12: T_5=temp/10; 
	L_13: temp= T_5;
	 L_14: goto L_4; 
	L_16: goto L_19; 
	L_17: printf ("num= %d', num);
	L_18: goto L_20; 
	L_19: printf ("num= %d', num);
	L_20: {}
	
}