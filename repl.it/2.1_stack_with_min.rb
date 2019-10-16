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

    if @head.nil?
      @head = new_node
      @min = @head.value
    else
      @tail.next_node = new_node
    end
    @tail = new_node
    @index += 1
    @min.append(new_node.value) if new_node.value < @min[-1]
  end

  def pop
    poped = @tail
    @tail = get_node(@index - 1)
    @tail.next_node = nil
    @index -= 1
    @head = nil if @index == -1
    poped.value
  end

  def min
    min = @head.value
    current = @head
    while current.next_node
      min = current.next_node.value if current.value > current.next_node.value
      current = current.next_node
    end
    min
  end

  private

  def get_node(index)
    node = @head

    while index.positive? && node
      node = node.next_node
      index -= 1
    end
    node
  end
end

stack = Stack.new
stack.push(3)
stack.push(5)
puts stack.min
# => 3

stack.pop
stack.push(7)
puts stack.min
# => 3

stack.push(2)
puts stack.min
# => 2

stack.pop
puts stack.min
# => 3
