# frozen_string_literal: true


class Node
  attr_accessor :value, :next_node

  def initialize(value, next_node = nil)
    @value = value
    @next_node = next_node
  end
end

class Queue

  def add(number)
    new_node = Node.new(number)

    if @head.nil?
      @head = new_node
    else
      @tail.next_node = new_node
    end
    @tail = new_node
  end

  def remove
    return -1 if @head.nil?

      poped = @head
      @head = @head.next_node
      poped.value
  end
end

queue = Queue.new

queue.add(3)
queue.add(5)
puts queue.remove
