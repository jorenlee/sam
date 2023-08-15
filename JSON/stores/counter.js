import { defineStore } from 'pinia'




export const useCounterStore = defineStore('counter', {
  state: () => {
    return { 
     count: 0,
     cars: {
      color: 'red',
      model: 'MB1023',
      brand: 'Toyota'
     } 
    }
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    increment() {
      this.count++
    },
  },
})