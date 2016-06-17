(define (square x)
  (* x x))

(define (abs x)
  (if (< x 0) (- x) x))

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (average x y)
  (/ (+ x y) 2))

(define (improve guess x)
  (average guess (/ x guess)))

(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x)
                 x)))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(define (cube x)
  (* x x x))

(define (average3 x y)
  (/ (+ (/ x (square y)) (* 2 y)) 3))

(define (factorial n)
  (if (= n 1)
      1
      (* n (factorial (- n 1)))))
