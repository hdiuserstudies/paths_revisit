import React, { useState } from 'react';

const generateParticipantId = (): string => {
  const randomNumber = Math.floor(1000 + Math.random() * 9000); // 4-digit number
  return `P${randomNumber}`;
};

const Pid: React.FC = () => {
  const [participantId] = useState<string>(() => generateParticipantId());

  return (
    <div className="p-4 rounded-xl shadow-md bg-white w-fit">
      <h2 className="text-xl font-semibold mb-2">{participantId}</h2>
    </div>
  );
};

export default Pid;
