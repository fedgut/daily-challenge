# frozen_string_literal: true

class Node
  attr_accessor :value, :next_node

  def initialize(value, next_node = nil)
    @value = value
    @next_node = next_node
  end
end

class Stack
  def initialize
    @index = -1
    @min = []
  end

  def push(number)
    new_node = Node.new(number)
    new_node.next_node = @head unless @head.nil?

    @head = new_node
    @min.push(@head.value) if @min.empty?

    @min.append(new_node.value) if new_node.value <= @min[-1]

    @index += 1
  end

  def pop
    poped = @head

    if @head.next_node
      @head = @head.next_node
    else
      @head = nil
    end
    @min.delete_at(-1) if poped.value == @min[-1]
    poped.value
  end

  def min
    @min[-1]
  end
end

stack = Stack.new
stack.push(3)
stack.push(5)
puts stack.pop
# => 5

stack.push(2)
stack.push(7)
puts stack.pop
# => 7

puts stack.pop
# => 2

puts stack.pop
# => 3
