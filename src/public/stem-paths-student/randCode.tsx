import React, { useState } from 'react';

const generateRandomCode = (length: number): string => {
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let result = '';
  const charactersLength = characters.length;

  for (let i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }

  return result;
};

const randCode: React.FC = () => {
  const [code, setCode] = useState<string>(() => generateRandomCode(8)); // default 8-character code

  const regenerateCode = () => {
    setCode(generateRandomCode(8));
  };

  return (
    <div className="p-4 rounded-xl shadow-md bg-white w-fit">
      <h2 className="text-xl font-semibold mb-2">{code}</h2>
    </div>
  );
};

export default randCode;
