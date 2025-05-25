import { useState, useEffect } from 'react';
import { Button, Box, Text } from '@mantine/core';
import { StimulusParams } from '../../../store/types';

function timer_pilot2({ setAnswer }: StimulusParams<unknown>) {
  const [timeLeft, setTimeLeft] = useState(300); // 5 minutes in seconds
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
    setIsRunning(true);
  };

  const formatTime = (seconds: number) => {
    const min = Math.floor(seconds / 60).toString().padStart(2, '0');
    const sec = (seconds % 60).toString().padStart(2, '0');
    return `${min}:${sec}`;
  };

  return (
    <Box style={{ textAlign: 'center', padding: '2rem' }}>
      <Text size="xl" mb="md">Timer: {formatTime(timeLeft)}</Text>

      {!isRunning && !timerDone && (
        <Button onClick={startTimer}>Start</Button>
      )}

      {timerDone && (
        <Text mt="md" color="green">
          Time's up! You may now proceed.
        </Text>
      )}

    </Box>
  );
}

export default timer_pilot2;
