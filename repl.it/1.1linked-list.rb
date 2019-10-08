# frozen_string_literal: true

class Node
  attr_accessor :value, :next_node

  def initialize(value, next_node = nil)
    @value = value
    @next_node = next_node
  end
end

class LinkedList
  attr_accessor :head, :tail

  def initialize(start_value = nil)
    @head = Node.new(start_value)
    @tail = @head
  end

  def add(number)
    if @head.value.nil?
      @head.value = number
      @head.next_node = @tail.value
    else
      @tail.next_node = Node.new(number)
      @tail = @tail.next_node
    end
  end

  def get(index)
    counter = 0
    current_node = @head
    until counter == index
      current_node = current_node.next_node
      return nil if current_node.nil?

      counter += 1
    end
    current_node.value
  end
end
