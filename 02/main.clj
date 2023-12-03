(ns main
  (:require
    [clojure.string :as str]))


(defn split-input-lines
  [fileName]
  (->> fileName
       slurp
       str/split-lines))


(defn getSets
  [setsText]
  (into {} (map #(let [s (str/split % #" ")] {(second s) (parse-long (first s))}) (str/split setsText #", "))))


(defn parseGame
  [currentGame]
  (let [gameId (parse-long (last (str/split (first (str/split currentGame #":")) #" ")))
        setsText (map str/trim (str/split (second (str/split currentGame #":")) #";"))
        finalSets (map getSets setsText)]
    {gameId finalSets}))


(defn checkGame
  [game]
  (and (<= (get game "green" 0) 13)
       (<= (get game "blue" 0) 14)
       (<= (get game "red" 0) 12)))


(defn possible
  [set]
  (every? checkGame (val set)))


(defn solution1
  [fileName]
  (->> fileName
       split-input-lines
       (into {} (map parseGame))
       (filter possible)
       (map key)
       (reduce +)))


(defn minNeeded
  [game]
  (reduce #(merge-with max %1 %2) {} game))


(defn power
  [values]
  (apply * (vals values)))


(defn solution2
  [fileName]
  (->> fileName
       split-input-lines
       (into {} (map parseGame))
       (vals)
       (map minNeeded)
       (map power)
       (reduce +)))


(println (solution1 "././test.txt"))
(println (solution1 "././input.txt"))
(println (solution2 "././test.txt"))
(println (solution2 "././input.txt"))
