# frozen_string_literal: true

class Node
  attr_accessor :value, :next_node

  def initialize(value, next_node = nil)
    @value = value
    @next_node = next_node
  end
end

class LinkedList
  # setup head and tail

  def add(number)
    # your code here
    new_node = Node.new(number)

    if @head.nil?
      @head = new_node
      @tail = new_node
    else
      @tail.next_node = new_node
      @tail = new_node
    end
  end

  def get(index)
    # your code here
    node = @head

    while index > 0 && node
      node = node.next_node
      index -= 1
    end

    node.value
  end
  
  def add_at(index, number)
      if index == 0  
        old_at_index = get_node(index) 
        @head = Node.new(number)
        @head.next_node = old_at_index
      else
        node = get_node(index-1)
        old_next = node.next_node
        new_next = Node.new(number)
        node.next_node = new_next 
        new_next.next_node = old_next
      end
  end
  
  def remove(index)
    if index == 0
      @head = @head.next_node
    else 
      prev = get_node(index-1)
      prev.next_node = prev.next_node.next_node
    end
  end
    
  
  private
  def get_node(index)
    node = @head
    
    while (index) > 0 && node
      node = node.next_node
      index -= 1
    end
    node
  end
  
end

list = LinkedList.new

list.add(3)
list.add(5)
list.add_at(1, 11)
list.add_at(0, 13)

puts list.get(2)
# => 11

puts list.get(3)
# => 5