class Gigasecond {
    public timestamp: number

    constructor (d: Date) {
        this.timestamp = d.getTime() + 1e12
    }
    date() {
        return new Date(this.timestamp)
    }
}

export default Gigasecond
