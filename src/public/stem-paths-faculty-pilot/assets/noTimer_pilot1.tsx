import { useState, useEffect } from 'react';
import { Button, Box, Modal, Checkbox } from '@mantine/core';
import ReactMarkdown from 'react-markdown';
import { StimulusParams } from '../../../store/types';

interface QuestionnaireParams {
  markdownText: string;
}

function TimedQuestionnaire({ setAnswer}: StimulusParams<QuestionnaireParams>) {
  const [showQuestionnaire, setShowQuestionnaire] = useState(false);
  const [selectedOption, setSelectedOption] = useState<string[]>([]);
  const [questionSubmitted, setQuestionSubmitted] = useState(false);
  const [modalOpened, setModalOpened] = useState(false);

  useEffect(() => {
    const timeout = setTimeout(() => {
      setShowQuestionnaire(true);
      setModalOpened(true);
    }, 30000);

    return () => clearTimeout(timeout);
  }, []);

  const handleSubmit = () => {
    if (selectedOption.length > 0) {
      setQuestionSubmitted(true);
      setModalOpened(false);
      if (setAnswer) {
        setAnswer({
          status: true,
          answers: {
            questionnaireAnswer: selectedOption,
          },
        });
      }
    }
  };

  return (
    <Box style={{ textAlign: 'left' }}>

      <Modal
        opened={modalOpened}
        onClose={() => {}}
        title=""
        withCloseButton={false}
        centered
      >
        <Box>
  <ReactMarkdown>
    {"Please identify the relevant math concepts with respect to the math problem (select all that apply)"}
  </ReactMarkdown>

          <Checkbox.Group value={selectedOption} onChange={setSelectedOption}>
            <Checkbox value="probability" label="Probability" />
            <Checkbox value="combinatorics" label="Combinatorics" />
            <Checkbox value="geometry" label="Geometry" />
            <Checkbox value="algebra" label="Algebra" />
            <Checkbox value="logic" label="Logic" />
            <Checkbox value="statistics" label="Statistics" />
            <Checkbox value="graph_theory" label="Graph Theory" />
            <Checkbox value="number_theory" label="Number Theory" />
            <Checkbox value="game_theory" label="Game Theory" />
            <Checkbox value="set_theory" label="Set Theory" />
          </Checkbox.Group>

          <Button mt="md" onClick={handleSubmit} disabled={selectedOption.length === 0}>
            Submit
          </Button>
        </Box>
      </Modal>

      {questionSubmitted}
    </Box>
  );
}

export default TimedQuestionnaire;