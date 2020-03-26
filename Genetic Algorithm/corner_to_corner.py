# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import math
import random
import turtle
from time import sleep

# Number of individuals in each generation
POPULATION_SIZE = 100

# Valid genes
GENES = ['r','d','u','l']

# Target string to be generated
TARGET = [20,20]

gnome_len = int(math.fabs(TARGET[0])+math.fabs(TARGET[1]))

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']
turtles = [turtle.Turtle() for i in range(10)]
#turtles = [turtle.Turtle()]
h = 0
for t in turtles:
	t.speed(1000)
	h+=1

wn = turtle.Screen()
wn.title("Paths")

class Individual(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(self,gnome_len = -1):

        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def create_gnome(self):

        global TARGET
        global gnome_len
        return [self.mutated_genes() for _ in range(gnome_len)]

    def mate(self, par2):

        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):

            prob = random.random()

            if prob < 0.49:
                child_chromosome.append(gp1)

            elif prob < 0.98 :
                child_chromosome.append(gp2)

            else:
                child_chromosome.append(self.mutated_genes())

        return Individual(child_chromosome)

    def cal_fitness(self):

        global TARGET
        location = [0,0]

        for direction in self.chromosome:
            if direction == 'r':
                location[1]+=1
            elif direction == 'l':
                location[1]-=1
            elif direction == 'u':
                location[0]-=1
            elif direction == 'd':
                location[0]+=1

        fitness = math.sqrt((TARGET[0]-location[0])**2+(TARGET[1]-location[1])**2)

        return fitness

def draw_population(population):

	#TESTING
	for t in turtles:
		t.speed(1000)
	turtles[0].color('red')

	point = turtle.Turtle()
	point.up()
	point.color('green')
	point.goto(200,-200)

	for i in range(gnome_len):
		
		for j in range(len(population)):
			if i==0:
				if population[j].chromosome[i]=='l':
					turtles[j].right(180)
				elif population[j].chromosome[i]=='u':
					turtles[j].left(90)
				elif population[j].chromosome[i]=='d':
					turtles[j].right(90)
				
			else:
				if population[j].chromosome[i]!=population[j].chromosome[i-1]:
					if population[j].chromosome[i-1]=='l' and population[j].chromosome[i]=='r':
						turtles[j].right(180)
					if population[j].chromosome[i-1]=='l' and population[j].chromosome[i]=='u':
						turtles[j].right(90)
					if population[j].chromosome[i-1]=='l' and population[j].chromosome[i]=='d':
						turtles[j].left(90)
					if population[j].chromosome[i-1]=='r' and population[j].chromosome[i]=='l':
						turtles[j].right(180)
					if population[j].chromosome[i-1]=='r' and population[j].chromosome[i]=='u':
						turtles[j].left(90)
					if population[j].chromosome[i-1]=='r' and population[j].chromosome[i]=='d':
						turtles[j].right(90)
					if population[j].chromosome[i-1]=='u' and population[j].chromosome[i]=='r':
						turtles[j].right(90)
					if population[j].chromosome[i-1]=='u' and population[j].chromosome[i]=='l':
						turtles[j].left(90)
					if population[j].chromosome[i-1]=='u' and population[j].chromosome[i]=='d':
						turtles[j].right(180)
					if population[j].chromosome[i-1]=='d' and population[j].chromosome[i]=='r':
						turtles[j].left(90)
					if population[j].chromosome[i-1]=='d' and population[j].chromosome[i]=='l':
						turtles[j].right(90)
					if population[j].chromosome[i-1]=='d' and population[j].chromosome[i]=='u':
						turtles[j].right(180)
			turtles[j].forward(10)
	sleep(3)
	wn.reset()

# Driver code
def main():
    global POPULATION_SIZE

    #current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for _ in range(POPULATION_SIZE):
                gnome = Individual.create_gnome()
                population.append(Individual(gnome))

    while not found:

        # sort the population in increasing order of fitness score
        population = sorted(population, key = lambda x:x.fitness)

        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
        if population[0].fitness <= 0:
            found = True
            break

        # Otherwise generate new offsprings for new generation
        new_generation = []

        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((5*POPULATION_SIZE)/100)
        new_generation.extend(population[:s])

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((95*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:10])
            parent2 = random.choice(population[:10])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        print("Generation: {}\tString: {}\tFitness: {}".\
              format(generation,
              "".join(population[0].chromosome),
              population[0].fitness))

        generation += 1
        draw_population(population[:10])

    print("Generation: {}\tString: {}\tFitness: {}".\
          format(generation,
          "".join(population[0].chromosome),
          population[0].fitness))
    draw_population([population[0]])

if __name__ == '__main__':
    main()
