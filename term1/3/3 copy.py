def tower(n,starting_rod,destination_rod, helper_rod):
	if n == 1:
		print(f"move disk {n} from {starting_rod} to {destination_rod}")
		return
	tower(n-1,starting_rod, helper_rod,destination_rod)
	print(f"move disk {n} from {starting_rod} to {destination_rod}")
	tower(n-1, helper_rod,destination_rod,starting_rod)
entered_number = int(input())
tower(entered_number, 'A', 'B', 'C')
