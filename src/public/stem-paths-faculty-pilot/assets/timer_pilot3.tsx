import { useState, useEffect } from 'react';
import { Button, Box, Text, NumberInput } from '@mantine/core';
import { StimulusParams } from '../../../store/types';

function CustomTimer({ setAnswer }: StimulusParams<unknown>) {
  const [inputMinutes, setInputMinutes] = useState<number | ''>('');
  const [timeLeft, setTimeLeft] = useState<number>(0);
  const [isRunning, setIsRunning] = useState(false);
  const [timerDone, setTimerDone] = useState(false);

  useEffect(() => {
    if (!isRunning) return;

    if (timeLeft <= 0) {
      setIsRunning(false);
      setTimerDone(true);
      if (setAnswer) {
        setAnswer({
          status: true,
          answers: {
            timerDone: true,
          },
        });
      }
      return;
    }

    const interval = setInterval(() => {
      setTimeLeft((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(interval);
  }, [isRunning, timeLeft, setAnswer]);

  const startTimer = () => {
    if (typeof inputMinutes === 'number' && inputMinutes > 0) {
      setTimeLeft(inputMinutes * 60); // convert to seconds
      setIsRunning(true);
    }
  };

  const formatTime = (seconds: number) => {
    const min = Math.floor(seconds / 60).toString().padStart(2, '0');
    const sec = (seconds % 60).toString().padStart(2, '0');
    return `${min}:${sec}`;
  };

  return (
    <Box style={{ textAlign: 'center', padding: '2rem', maxWidth: 300, margin: 'auto' }}>
      {!isRunning && !timerDone && (
        <Box mb="md">
          <NumberInput
            label="Enter timer duration (minutes)"
            value={inputMinutes}
            onChange={(value) => setInputMinutes(typeof value === 'number' ? value : '')}
            min={1}
            max={120}
            step={1}
          />
        </Box>
      )}

      <Text size="xl" mb="md">
        Timer: {formatTime(timeLeft)}
      </Text>

      {!isRunning && !timerDone && (
        <Button onClick={startTimer} disabled={typeof inputMinutes !== 'number' || inputMinutes <= 0}>
          Start
        </Button>
      )}

      {timerDone && (
        <Text mt="md" color="green">
          Time's up! You may now proceed.
        </Text>
      )}

    </Box>
  );
}

export default CustomTimer;
